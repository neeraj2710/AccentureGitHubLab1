# Token Generator API

A Python FastAPI application that generates pseudo-random tokens and tokenizes text input.

## Features

- **Random Token Generation**: Generate secure random tokens for identification purposes
- **Text Tokenization**: Split text into tokens and calculate checksums
- **Interactive API**: RESTful endpoints with JSON responses

## Prerequisites

- Python 3.8+
- FastAPI
- Uvicorn
- Pydantic

## Installation

1. Install required dependencies:
```bash
pip install fastapi uvicorn pydantic
```

## How to Run

Start the application using Uvicorn web server:
```bash
uvicorn main:app --reload
```

The API will be available at: `http://127.0.0.1:8000`

## API Endpoints

### 1. Welcome Message
- **URL**: `/`
- **Method**: `GET`
- **Description**: Returns a welcome message
- **Response**:
```json
{
  "message": "Welcome to Token Generator API by Neeraj Wadhwaney!",
  "description": "This API generates tokens and processes text"
}
```

### 2. Generate Token
- **URL**: `/generate`
- **Method**: `GET`
- **Description**: Generates a random hexadecimal token
- **Response**:
```json
{
  "token": "a1b2c3d4e5f6..."
}
```

### 3. Tokenize Text
- **URL**: `/tokenize`
- **Method**: `POST`
- **Description**: Accepts text and returns tokens with checksum
- **Request Body**:
```json
{
  "text": "your text here"
}
```
- **Response**:
```json
{
  "tokens": ["your", "text", "here"],
  "count": 3,
  "checksum": "sha256_hash_here"
}
```

## Running Tests

Execute test cases using pytest:
```bash
pytest test_main.py -v
```

## API Documentation

Once the server is running, access:
- **Swagger UI**: http://127.0.0.1:8000/docs
- **ReDoc**: http://127.0.0.1:8000/redoc

## Author

Developed by Neeraj Wadhwaney using GitHub Copilot assistance

## Technologies Used

- FastAPI
- Python 3.8+
- Pydantic
- Uvicorn
- GitHub Copilot
