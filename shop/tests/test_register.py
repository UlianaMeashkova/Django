import requests

def test_register():
    response = requests.get("http://127.0.0.1:8000/register")
    assert response.status_code == 200
    assert "Register user" in str(response.content)

def test_register_password():
    response = requests.get("http://127.0.0.1:8000/register")
    assert response.status_code == 200
    assert "Password" in str(response.content)