from fastapi.testclient import TestClient
from main import app

# Create test client
client = TestClient(app)

def test_welcome():
    """Test the welcome endpoint"""
    response = client.get("/")
    assert response.status_code == 200
    assert "message" in response.json()
    assert "Neeraj Wadhwaney" in response.json()["message"]

def test_generate_token():
    """Test the token generation endpoint"""
    response = client.get("/generate")
    assert response.status_code == 200
    assert "token" in response.json()
    assert len(response.json()["token"]) == 32  # hex token is 32 chars

def test_tokenize_text():
    """Test the tokenize endpoint with sample text"""
    test_data = {"text": "hello world from python"}
    response = client.post("/tokenize", json=test_data)
    
    assert response.status_code == 200
    assert "tokens" in response.json()
    assert "count" in response.json()
    assert "checksum" in response.json()
    assert response.json()["count"] == 4
    assert response.json()["tokens"] == ["hello", "world", "from", "python"]

def test_tokenize_empty_text():
    """Test tokenize endpoint with empty text"""
    test_data = {"text": ""}
    response = client.post("/tokenize", json=test_data)
    
    assert response.status_code == 200
    assert response.json()["count"] == 1  # Empty string split gives ['']

def test_tokenize_single_word():
    """Test tokenize endpoint with single word"""
    test_data = {"text": "python"}
    response = client.post("/tokenize", json=test_data)
    
    assert response.status_code == 200
    assert response.json()["count"] == 1
    assert response.json()["tokens"] == ["python"]
