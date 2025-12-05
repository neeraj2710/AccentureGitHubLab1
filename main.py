from fastapi import FastAPI
from pydantic import BaseModel
import hashlib
import secrets

app = FastAPI()

# Pydantic model for text input
class TextInput(BaseModel):
    text: str

def generate():
    """
    Generate a random token for identification purposes
    Returns a hexadecimal string token
    """
    return secrets.token_hex(16)

@app.get("/")
def welcome():
    """
    Welcome endpoint with customized message
    Returns a welcome message with participant name
    """
    return {
        "message": "Welcome to Token Generator API by Neeraj Wadhwaney!",
        "description": "This API generates tokens and processes text"
    }

@app.get("/generate")
def generate_token():
    """
    Endpoint to generate a random token
    Returns a JSON response with the generated token
    """
    token = generate()
    return {"token": token}

@app.post("/tokenize")
async def tokenize_text(input_data: TextInput):
    """
    Endpoint that accepts text via POST request and returns tokens
    
    Parameters:
    - text (str): Input text to be tokenized
    
    Returns:
    - tokens (list): List of words/tokens from the input text
    - count (int): Number of tokens
    - checksum (str): SHA256 checksum of the input text
    """
    # Split text into tokens
    tokens = input_data.text.split()
    
    # Generate checksum of the text
    checksum = hashlib.sha256(input_data.text.encode()).hexdigest()
    
    return {
        "tokens": tokens,
        "count": len(tokens),
        "checksum": checksum
    }
