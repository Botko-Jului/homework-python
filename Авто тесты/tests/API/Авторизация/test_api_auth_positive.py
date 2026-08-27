import pytest

class TestAuthRequestCode:
    def test_request_code_valid_email(self, api_client, base_url, new_user_data, auth_data):
        response = api_client.post(
            f"{base_url}/api/auth/request-code",
            json={"email": new_user_data.email}
        )
        assert response.status_code == 200
        data = response.json()
        assert data["email"] == new_user_data.email
        assert "code" in data
        assert len(data["code"]) > 0
        assert data["message"] is not None
        
        # Сохраняем в общий словарь
        auth_data["email"] = data["email"]
        auth_data["code"] = data["code"]
        
        print(f"\n✅ Код сохранен: {auth_data['code']}")
        print(f"✅ Email сохранен: {auth_data['email']}")