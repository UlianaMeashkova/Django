import requests
from django.test.client import Client

def test_products_index():
    response = requests.get("http://127.0.0.1:8000")
    assert response.status_code == 200
    assert "Product" in str(response.content)

  
class TestIndex:
    def setup_method(self):
        self.client = Client()

    def test_index(self):
        response = self.client.get("/")
        assert response.status_code == 200
