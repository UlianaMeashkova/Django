import requests

def test_products_index():
    response = requests.get("http://127.0.0.1:8000")
    assert response.status_code == 200
    assert "Product:" in str(response.content)
