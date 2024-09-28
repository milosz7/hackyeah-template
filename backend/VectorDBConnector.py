from langchain_pinecone import PineconeVectorStore
from pinecone import Pinecone
from langchain.embeddings.huggingface import HuggingFaceEmbeddings
import os


class VectorDBConnector:
    def __init__(self, index_name, model_name):
        pc = Pinecone(api_key=os.environ.get("PINECONE_API"))
        embeddings = HuggingFaceEmbeddings(model_name=model_name)
        index = pc.Index(index_name)
        self.vector_store = PineconeVectorStore(index=index, embedding=embeddings)


    def find_simillar(self, text):
        return self.vector_store.similarity_search(text, k=1)
