import pytest

import pytest


class TestAuthRequestCodeNegative:
    
    def test_request_code_invalid_email(self, api_client, base_url, invalid_email):
        response = api_client.post(
            f"{base_url}/api/auth/request-code",
            json={"email": invalid_email}
        )
        assert response.status_code == 400
        assert "error" in response.json() or "message" in response.json()

    def test_request_code_empty_email(self, api_client, base_url):
        response = api_client.post(
            f"{base_url}/api/auth/request-code",
            json={"email": ""}
        )
        assert response.status_code == 400

    def test_request_code_int_email(self, api_client, base_url):
        response = api_client.post(
            f"{base_url}/api/auth/request-code",
            json={"email": 12345}
        )
        assert response.status_code == 400

    def test_request_code_null_email(self, api_client, base_url):
        response = api_client.post(
            f"{base_url}/api/auth/request-code",
            json={"email": None}
        )
        assert response.status_code == 400

    def test_request_code_missing_email(self, api_client, base_url):
        response = api_client.post(
            f"{base_url}/api/auth/request-code",
            json={}
        )
        assert response.status_code == 400

    def test_request_code_extra_fields(self, api_client, base_url, new_user_data):
        response = api_client.post(
            f"{base_url}/api/auth/request-code",
            json={
                "email": new_user_data.email,
                "role": "superuser"
            }
        )
        assert response.status_code == 200
        assert "code" in response.json()


