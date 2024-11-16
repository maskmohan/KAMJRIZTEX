from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_scrape_endpoint():
    response = client.get("/scrape")
    assert response.status_code == 200

def test_data_endpoint():
    response = client.get("/data")
    assert response.status_code == 200
