from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.docstore.document import Document
import re
import bs4
import requests
import os
from pinecone import Pinecone, ServerlessSpec
from langchain_pinecone import PineconeVectorStore
from langchain.embeddings.huggingface import HuggingFaceEmbeddings
from dotenv import load_dotenv, find_dotenv
import time


if __name__ == "__main__":
    load_dotenv(find_dotenv())

    urls = ['https://www.podatki.gov.pl/pcc-sd/abc-pcc/czynnosci-cywilnoprawne-nieopodatkowane-pcc/',
            'https://www.podatki.gov.pl/pcc-sd/abc-pcc/sposob-zaplaty-podatku-pcc/',
            'https://www.podatki.gov.pl/pcc-sd/abc-pcc/obowiazek-podatkowy-pcc/',
            'https://www.podatki.gov.pl/wyszukiwarki/wyszukiwarka-teleadresowa-jednostek-kas/',
            'https://www.podatki.gov.pl/pcc-sd/abc-pcc/zwolnienia-pcc/',
            'https://www.podatki.gov.pl/pcc-sd/rozliczenie-podatku-pcc-od-kupna-samochodu/',
            'https://www.podatki.gov.pl/pcc-sd/abc-pcc/stawki-podatkowe-pcc/',
            'https://www.podatki.gov.pl/pcc-sd/abc-pcc/kto-jest-podatnikiem-a-kto-platnikiem-pcc/',
            'https://www.podatki.gov.pl/pcc-sd/abc-pcc/organy-podatkowe-pcc/',
            'https://www.podatki.gov.pl/pcc-sd/rozliczenie-podatku-pcc-od-pozyczki/',
            'https://www.podatki.gov.pl/pcc-sd/rozliczenie-podatku-pcc-od-innych-czynnosci/',
            'https://www.podatki.gov.pl/pcc-sd/abc-pcc/przedmiot-opodatkowania-pcc/'
            ]

    relevant_texts = []

    for url in urls:
        response = requests.get(url)
        if response.status_code == 200:
            soup = bs4.BeautifulSoup(response.text, "html.parser")
            section = soup.find("section", class_="article-content")
            if section:
                relevant_text = section.get_text()
            else:
                relevant_text = soup.get_text()
            
            relevant_text = relevant_text.replace("\n", " ")
            relevant_text = re.sub(r"\s{2,}", " ", relevant_text)
            relevant_texts.append(relevant_text)

    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=500,
        chunk_overlap=30 
    )

    chunked_docs = []
    for text in relevant_texts:
        chunks = text_splitter.split_text(text)
        for chunk in chunks:
            chunked_docs.append(Document(page_content=chunk))

    pc = Pinecone(api_key=os.environ.get("PINECONE_API"))

    index_name = "hackyeah-pcc" 

    existing_indexes = [index_info["name"] for index_info in pc.list_indexes()]

    model_name = "sdadas/st-polish-paraphrase-from-distilroberta"
    embeddings = HuggingFaceEmbeddings(model_name=model_name)

    if index_name not in existing_indexes:
        pc.create_index(
            name=index_name,
            dimension=768,
            metric="cosine",
            spec=ServerlessSpec(cloud="aws", region="us-east-1"),
        )
        while not pc.describe_index(index_name).status["ready"]:
            time.sleep(1)

    index = pc.Index(index_name)
    vector_store = PineconeVectorStore(index=index, embedding=embeddings)

    vector_store.add_documents(chunked_docs)
    