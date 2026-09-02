import pytest


class TestProfilePatchPositive:

    # редактирование города
    def test_profile_patch_city(self, api_client, base_url, full_user_data):
        token = full_user_data.token
        headers = {"Authorization": f"Bearer {token}"}
        
        new_city = "Казань"
        response = api_client.patch(
            f"{base_url}/api/profile",
            json={"city": new_city},
            headers=headers
        )
        
        assert response.status_code == 200
        data = response.json()
        assert data["city"] == new_city
        assert data["first_name"] == full_user_data.first_name
        assert data["last_name"] == full_user_data.last_name
        assert data["age"] == full_user_data.age
        
        print(f"\n✅ Город изменен на: {new_city}")

    # редактирование имени
    def test_profile_patch_first_name(self, api_client, base_url, full_user_data):
        token = full_user_data.token
        headers = {"Authorization": f"Bearer {token}"}
        
        new_name = "Александр"
        response = api_client.patch(
            f"{base_url}/api/profile",
            json={"first_name": new_name},
            headers=headers
        )
        
        assert response.status_code == 200
        data = response.json()
        assert data["first_name"] == new_name
        assert data["city"] == full_user_data.city
        assert data["last_name"] == full_user_data.last_name
        
        print(f"\n✅ Имя изменено на: {new_name}")

    # редактирование возраста
    def test_profile_patch_age(self, api_client, base_url, full_user_data):
        token = full_user_data.token
        headers = {"Authorization": f"Bearer {token}"}
        
        new_age = 30
        response = api_client.patch(
            f"{base_url}/api/profile",
            json={"age": new_age},
            headers=headers
        )
        
        assert response.status_code == 200
        data = response.json()
        assert data["age"] == new_age
        assert data["first_name"] == full_user_data.first_name
        assert data["city"] == full_user_data.city
        
        print(f"\n✅ Возраст изменен на: {new_age}")

    # редактирование нескольких полей сразу
    def test_profile_patch_multiple_fields(self, api_client, base_url, full_user_data):
        token = full_user_data.token
        headers = {"Authorization": f"Bearer {token}"}
        
        new_data = {
            "first_name": "Петр",
            "city": "Сочи",
            "bio": "Новое описание"
        }
        response = api_client.patch(
            f"{base_url}/api/profile",
            json=new_data,
            headers=headers
        )
        
        assert response.status_code == 200
        data = response.json()
        assert data["first_name"] == new_data["first_name"]
        assert data["city"] == new_data["city"]
        assert data["bio"] == new_data["bio"]
        assert data["last_name"] == full_user_data.last_name
        assert data["age"] == full_user_data.age
        
        print(f"\n✅ Несколько полей изменено: {new_data}")