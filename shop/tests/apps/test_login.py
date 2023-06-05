import requests


def test_login():
    response = requests.get("http://127.0.0.1:8000/login")
    assert response.status_code == 200
    assert "Login user" in str(response.content)
