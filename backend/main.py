from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

import xml.etree.ElementTree as ET
from json_to_xml import json_to_xml
from dto.declaration import DeclarationDTO

app = FastAPI()
origins = ["http://localhost:4200"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def read_root():
    return {"data": "Hello World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: str | None = None):
    return {"item_id": item_id, "q": q}

@app.get("/xml")
def get_xml():
    
    json_data = '''
    {
        "note": {
            "to": "dsajdvasjhdva",
            "from": "Jani",
            "heading": "Reminder",
            "body": "Don't forget me this weekend!"
        }
    }
    '''

    xml = json_to_xml(json_data, "Deklaracja")

    return xml
