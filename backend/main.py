from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
import xml.etree.ElementTree as ET
from json_to_xml import json_to_xml
from dto.DeclarationDTO import DeclarationDTO
from typing import List, Dict, Optional
import uuid
from enum import Enum
from datetime import datetime
from pydantic import BaseModel

app = FastAPI()

origins = ["http://localhost:4200"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# Dictionary to hold user data and conversations
users_conversations: Dict[uuid.UUID, Dict[uuid.UUID, "Conversation"]] = {}
users_data: Dict[uuid.UUID, "UserDTO"] = {}

# Enum to define the source of the message (user or model)
class MessageSource(str, Enum):
    user = "user"
    model = "model"

# Define the Message DTO with source, time, and message content
class MessageDTO(BaseModel):
    conversation_id: uuid.UUID
    time: datetime
    source: MessageSource
    message: str

# Define the Conversation DTO (with messages being a list of MessageDTO)
class Conversation(BaseModel):
    user_id: uuid.UUID
    conversation_id: uuid.UUID
    messages: List[MessageDTO]

# Define the User DTO with a list of conversations
class UserDTO(BaseModel):
    user_id: uuid.UUID
    user_name: str
    conversations: List[Conversation]

dummy_user_id = uuid.uuid4()
dummy_conversation_id = uuid.uuid4()

dummy_user = UserDTO(
    user_id=dummy_user_id,
    user_name="test_user",
    conversations=[]
)

dummy_message = MessageDTO(
    conversation_id=dummy_conversation_id,
    time=datetime.now(),
    source=MessageSource.user,
    message="This is a dummy message"
)

dummy_conversation = Conversation(
    user_id=dummy_user_id,
    conversation_id=dummy_conversation_id,
    messages=[dummy_message]
)

# Endpoint to create a new user
@app.post("/users", response_model=UserDTO)
async def create_user(user_name: str):
    # Generate a new user ID
    user_id = uuid.uuid4()
    
    # Initialize an empty list of conversations for the user
    new_user = UserDTO(
        user_id=user_id,
        user_name=user_name,
        conversations=[]
    )
    
    # Store the new user data in users_data and initialize their conversations in users_conversations
    users_data[user_id] = new_user
    users_conversations[user_id] = {}
    
    return dummy_user

# Endpoint to get a user by user_id
@app.get("/users/{user_id}", response_model=UserDTO)
async def get_user(user_id: uuid.UUID):
    user = users_data.get(user_id)
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return dummy_user

# Endpoint to create a new conversation for a user
@app.post("/user/{user_id}/conversations", response_model=Conversation)
async def create_conversation(user_id: uuid.UUID):
    # Check if the user exists, otherwise return 404
    user_conversations = users_conversations.get(user_id)
    if user_conversations is None:
        raise HTTPException(status_code=404, detail="User not found")
    
    # Generate a new conversation ID
    new_conversation_id = uuid.uuid4()
    
    # Create an empty conversation (you can modify this to include an initial message if desired)
    new_conversation = Conversation(
        user_id=user_id,
        conversation_id=new_conversation_id,
        messages=[]
    )
    
    # Store the new conversation in the user's conversations
    user_conversations[new_conversation_id] = new_conversation
    
    # Add the conversation to the user's data
    users_data[user_id].conversations.append(new_conversation)
    
    return dummy_conversation

# Endpoint to get a conversation by user_id and conversation_id
@app.get("/user/{user_id}/conversations/{conversation_id}", response_model=Conversation)
async def get_conversation(user_id: uuid.UUID, conversation_id: uuid.UUID):
    # Find the user's conversations
    user_conversations = users_conversations.get(user_id)
    if user_conversations is None:
        raise HTTPException(status_code=404, detail="User not found")
    
    # Find the conversation with the conversation_id
    conversation = user_conversations.get(conversation_id)
    if conversation is None:
        raise HTTPException(status_code=404, detail="Conversation not found")
    
    return dummy_conversation

@app.post("/user/{user_id}/conversations/{conversation_id}", response_model=Conversation)
async def post_message(user_id: uuid.UUID, conversation_id: uuid.UUID, message: str):
    user_conversations = users_conversations.get(user_id)
    
    if user_conversations is None:
        raise HTTPException(status_code=404, detail="User not found")
    
    # Find the conversation with the conversation_id
    conversation = user_conversations.get(conversation_id)
    
    if conversation is None:
        raise HTTPException(status_code=404, detail="Conversation not found")
    
    # Create and add the new message
    new_message = MessageDTO(
        conversation_id=conversation_id,
        time=datetime.now(),
        source=MessageSource.user,  # Assuming this is a user message for now
        message=message
    )
    
    conversation.messages.append(new_message)
    
    return dummy_message

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

@app.post("/submit-declaration")
async def submit_declaration(declaration: DeclarationDTO):

    return {
        "message": "Deklaracja zos(tała złożona pomyślnie!",
        "declaration": declaration
    }
