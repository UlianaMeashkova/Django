import pytest

from rest_framework.authtoken.admin import User
from rest_framework.authtoken.models import Token
from rest_framework.test import APIClient


@pytest.mark.django_db
class TestProductsApi:
    def setup_method(self):
        self.client = APIClient()
        self.data = {
            "email": "test@test.com",
            "password": "pa55word",
        }

    def test_auth(self):
        response = self.client.post("/api/register/", data=self.data)
        assert response.status_code == 201
        assert User.objects.exists()

        response = self.client.post("/api/login/", data=self.data)
        assert response.status_code == 200
        assert response.json().get("token") is not None
        assert Token.objects.exists()

        self.client.credentials(
            HTTP_AUTHORIZATION=f"Token {response.json().get('token')}"
        )
        response = self.client.delete("/api/logout/")
        assert response.status_code == 200
        assert not Token.objects.exists()
