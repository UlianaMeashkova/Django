import requests

def test_profiles():
    response = requests.get("http://127.0.0.1:8000/profiles")
    assert response.status_code == 200
    assert "Profiles view" in str(response.content)
