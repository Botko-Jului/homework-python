import pytest


class TestProfilePatchNegative:

    # без токена
    def test_profile_patch_without_token(self, api_client, base_url):
        response = api_client.patch(
            f"{base_url}/api/profile",
            json={"city": "Казань"}
        )
        assert response.status_code == 401

    # невалидный токен
    def test_profile_patch_invalid_token(self, api_client, base_url, invalid_token):
        headers = {"Authorization": f"Bearer {invalid_token}"}
        response = api_client.patch(
            f"{base_url}/api/profile",
            json={"city": "Казань"},
            headers=headers
        )
        assert response.status_code == 401

    # пустой токен
    def test_profile_patch_empty_token(self, api_client, base_url):
        headers = {"Authorization": "Bearer "}
        response = api_client.patch(
            f"{base_url}/api/profile",
            json={"city": "Казань"},
            headers=headers
        )
        assert response.status_code == 401

    # возраст 0
    def test_profile_patch_age_zero(self, api_client, base_url, new_registered_user):
        token = new_registered_user.token
        headers = {"Authorization": f"Bearer {token}"}
        
        # Заполняем анкету
        data = {
            "first_name": new_registered_user.first_name,
            "last_name": new_registered_user.last_name,
            "age": 25,
            "city": new_registered_user.city,
            "bio": new_registered_user.bio or "Тест"
        }
        api_client.post(
            f"{base_url}/api/questionnaire",
            json=data,
            headers=headers
        )
        
        response = api_client.patch(
            f"{base_url}/api/profile",
            json={"age": 0},
            headers=headers
        )
        assert response.status_code == 400

    # отрицательный возраст
    def test_profile_patch_age_negative(self, api_client, base_url, new_registered_user):
        token = new_registered_user.token
        headers = {"Authorization": f"Bearer {token}"}
        
        data = {
            "first_name": new_registered_user.first_name,
            "last_name": new_registered_user.last_name,
            "age": 25,
            "city": new_registered_user.city,
            "bio": new_registered_user.bio or "Тест"
        }
        api_client.post(
            f"{base_url}/api/questionnaire",
            json=data,
            headers=headers
        )
        
        response = api_client.patch(
            f"{base_url}/api/profile",
            json={"age": -5},
            headers=headers
        )
        assert response.status_code == 400

    # возраст больше 119
    def test_profile_patch_age_too_high(self, api_client, base_url, new_registered_user):
        token = new_registered_user.token
        headers = {"Authorization": f"Bearer {token}"}
        
        data = {
            "first_name": new_registered_user.first_name,
            "last_name": new_registered_user.last_name,
            "age": 25,
            "city": new_registered_user.city,
            "bio": new_registered_user.bio or "Тест"
        }
        api_client.post(
            f"{base_url}/api/questionnaire",
            json=data,
            headers=headers
        )
        
        response = api_client.patch(
            f"{base_url}/api/profile",
            json={"age": 150},
            headers=headers
        )
        assert response.status_code == 400

    # возраст 120
    def test_profile_patch_age_120(self, api_client, base_url, new_registered_user):
        token = new_registered_user.token
        headers = {"Authorization": f"Bearer {token}"}
        
        data = {
            "first_name": new_registered_user.first_name,
            "last_name": new_registered_user.last_name,
            "age": 25,
            "city": new_registered_user.city,
            "bio": new_registered_user.bio or "Тест"
        }
        api_client.post(
            f"{base_url}/api/questionnaire",
            json=data,
            headers=headers
        )
        
        response = api_client.patch(
            f"{base_url}/api/profile",
            json={"age": 120},
            headers=headers
        )
        assert response.status_code == 400

    # возраст строкой
    def test_profile_patch_age_string(self, api_client, base_url, new_registered_user):
        token = new_registered_user.token
        headers = {"Authorization": f"Bearer {token}"}
        
        data = {
            "first_name": new_registered_user.first_name,
            "last_name": new_registered_user.last_name,
            "age": 25,
            "city": new_registered_user.city,
            "bio": new_registered_user.bio or "Тест"
        }
        api_client.post(
            f"{base_url}/api/questionnaire",
            json=data,
            headers=headers
        )
        
        response = api_client.patch(
            f"{base_url}/api/profile",
            json={"age": "двадцать пять"},
            headers=headers
        )
        assert response.status_code == 400

    # пустое имя
    def test_profile_patch_empty_first_name(self, api_client, base_url, new_registered_user):
        token = new_registered_user.token
        headers = {"Authorization": f"Bearer {token}"}
        
        data = {
            "first_name": new_registered_user.first_name,
            "last_name": new_registered_user.last_name,
            "age": 25,
            "city": new_registered_user.city,
            "bio": new_registered_user.bio or "Тест"
        }
        api_client.post(
            f"{base_url}/api/questionnaire",
            json=data,
            headers=headers
        )
        
        response = api_client.patch(
            f"{base_url}/api/profile",
            json={"first_name": ""},
            headers=headers
        )
        assert response.status_code == 400

    # пустая фамилия
    def test_profile_patch_empty_last_name(self, api_client, base_url, new_registered_user):
        token = new_registered_user.token
        headers = {"Authorization": f"Bearer {token}"}
        
        data = {
            "first_name": new_registered_user.first_name,
            "last_name": new_registered_user.last_name,
            "age": 25,
            "city": new_registered_user.city,
            "bio": new_registered_user.bio or "Тест"
        }
        api_client.post(
            f"{base_url}/api/questionnaire",
            json=data,
            headers=headers
        )
        
        response = api_client.patch(
            f"{base_url}/api/profile",
            json={"last_name": ""},
            headers=headers
        )
        assert response.status_code == 400