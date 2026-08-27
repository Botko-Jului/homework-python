import pytest

class TestAuthVerify:
    def test_verify_correct_code(self, api_client, base_url, new_user_data, auth_data):
        # Берем сохраненный код
        email = auth_data["email"]
        code = auth_data["code"]

        print(f"\n📧 Email из сохраненных: {email}")
        print(f"🔑 Код из сохраненных: {code}")

        # 2. Проверка кода
        response = api_client.post(
            f"{base_url}/api/auth/verify",
            json={"email": email, "code": code}
        )
        
        assert response.status_code == 200
        data = response.json()
        assert "token" in data
        
        auth_data["token"] = data["token"]
        print(f"✅ Токен сохранен: {auth_data['token'][:30]}...")