from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
import xml.etree.ElementTree as ET
from json_to_xml import json_to_xml
from dto.DeclarationDTO import DeclarationDTO
from typing import List, Dict, Optional
import uuid
from enum import Enum
from datetime import datetime, timedelta
from pydantic import BaseModel
from passlib.context import CryptContext
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
import jwt

app = FastAPI()

origins = ["http://localhost:4200"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# to get a string like this run:
# openssl rand -hex 32
SECRET_KEY = "e85d5a41fb2fb4e4712ce13ccbecf44b6f648216427ac166f7553ecfb6ca7bda"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


# Enum to define the source of the message (user or model)
class MessageSource(str, Enum):
    user = "user"
    model = "model"

# Define the Message DTO with source, time, and message content
class Message(BaseModel):
    time: datetime
    source: MessageSource
    message: str

# Define the Conversation DTO (with messages being a list of MessageDTO)
class Conversation(BaseModel):
    conversation_id: uuid.UUID
    messages: List[Message]

# Define the User DTO with a list of conversations
class User(BaseModel):
    user_name: str
    conversations: List[Conversation]
class UserInDB(User):
    hashed_password: str

# Dictionary to hold user data and conversations
users_conversations: Dict[User, List[Conversation]] = {}



dummy_user_id = uuid.uuid4()
dummy_conversation_id = uuid.uuid4()
dummy_user = UserInDB(
    user_id=dummy_user_id,
    user_name="test_user",
    conversations=[],
    hashed_password = "asd"
)

dummy_message = Message(
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

#Database
#########################
def find_user_by_id(user_name):
    return dummy_user

def get_user_conversations(user_name):
    return [dummy_conversation]
def get_user_conversation_by_id(user_name,):
    return [dummy_conversation]
def save_user(user: UserInDB):
    print("saved user")
    
def delete_user_by_id(user_name):
    print("deleted user")
##########################

def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)


def get_password_hash(password):
    return pwd_context.hash(password)

@app.post("/register", response_model=User)
async def register_user(username: str, password: str):
    
    user = find_user_by_id(username)
    if username is not None:
        raise HTTPException(status_code=400, detail="Username already exists!")
    
    hashed_password = get_password_hash(password)
    
    new_user = UserInDB(
        user_name=username,
        hashed_password=hashed_password,
        conversations=[]
    )
    save_user(new_user)    
    return new_user


@app.post("/login")
async def login_user(form_data: OAuth2PasswordRequestForm = Depends()):
    user = find_user_by_id(form_data.username)
    if not user or not verify_password(form_data.password, user.hashed_password):
        raise HTTPException(status_code=400, detail="Invalid username or password")
    
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"sub": user.user_name}, expires_delta=access_token_expires
    )
    return {"access_token": access_token, "token_type": "bearer"}

# Endpoint to get a user by user_id
@app.get("/users/{user_id}", response_model=User)
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
    new_message = Message(
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
        "message": "Deklaracja została złożona pomyślnie!",
        "activityDate": declaration.activityDate,
        "submissionDate": declaration.submissionDate,
    }
