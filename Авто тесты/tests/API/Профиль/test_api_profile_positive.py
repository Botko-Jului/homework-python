import pytest


class TestProfilePositive:
    
    def test_get_profile_success(self, api_client, base_url, auth_data):
       
        
        token = auth_data["token"]
        email = auth_data["email"]
        
        headers = {"Authorization": f"Bearer {token}"}
        
        response = api_client.get(
            f"{base_url}/api/profile",
            headers=headers
        )
        
        assert response.status_code == 200
        data = response.json()
        assert data["email"] == email
        assert "first_name" in data
        assert "last_name" in data
        assert "age" in data
        assert "city" in data
        assert "bio" in data
        
        print(f"\n✅ Профиль получен для: {email}")
        print(f"   Имя: {data['first_name']}")
        print(f"   Фамилия: {data['last_name']}")
        print(f"   Возраст: {data['age']}")
        print(f"   Город: {data['city']}")