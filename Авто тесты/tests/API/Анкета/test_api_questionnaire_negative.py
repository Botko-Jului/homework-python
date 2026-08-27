import pytest


class TestQuestionnaireNegative:

    # пустое имя
    def test_questionnaire_empty_first_name(self, api_client, base_url, new_registered_user):
        token = new_registered_user.token
        headers = {"Authorization": f"Bearer {token}"}
        
        data = {
            "first_name": "",
            "last_name": new_registered_user.last_name,
            "age": 25,
            "city": new_registered_user.city,
            "bio": new_registered_user.bio or "Тест"
        }
        response = api_client.post(
            f"{base_url}/api/questionnaire",
            json=data,
            headers=headers
        )
        assert response.status_code == 400

    # пустая фамилия
    def test_questionnaire_empty_last_name(self, api_client, base_url, new_registered_user):
        token = new_registered_user.token
        headers = {"Authorization": f"Bearer {token}"}
        
        data = {
            "first_name": new_registered_user.first_name,
            "last_name": "",
            "age": 25,
            "city": new_registered_user.city,
            "bio": new_registered_user.bio or "Тест"
        }
        response = api_client.post(
            f"{base_url}/api/questionnaire",
            json=data,
            headers=headers
        )
        assert response.status_code == 400

    # пустой город
    def test_questionnaire_empty_city(self, api_client, base_url, new_registered_user):
        token = new_registered_user.token
        headers = {"Authorization": f"Bearer {token}"}
        
        data = {
            "first_name": new_registered_user.first_name,
            "last_name": new_registered_user.last_name,
            "age": 25,
            "city": "",
            "bio": new_registered_user.bio or "Тест"
        }
        response = api_client.post(
            f"{base_url}/api/questionnaire",
            json=data,
            headers=headers
        )
        assert response.status_code == 400

    # возраст 0
    def test_questionnaire_age_zero(self, api_client, base_url, new_registered_user):
        token = new_registered_user.token
        headers = {"Authorization": f"Bearer {token}"}
        
        data = {
            "first_name": new_registered_user.first_name,
            "last_name": new_registered_user.last_name,
            "age": 0,
            "city": new_registered_user.city,
            "bio": new_registered_user.bio or "Тест"
        }
        response = api_client.post(
            f"{base_url}/api/questionnaire",
            json=data,
            headers=headers
        )
        assert response.status_code == 400

    # отрицательный возраст
    def test_questionnaire_age_negative(self, api_client, base_url, new_registered_user):
        token = new_registered_user.token
        headers = {"Authorization": f"Bearer {token}"}
        
        data = {
            "first_name": new_registered_user.first_name,
            "last_name": new_registered_user.last_name,
            "age": -5,
            "city": new_registered_user.city,
            "bio": new_registered_user.bio or "Тест"
        }
        response = api_client.post(
            f"{base_url}/api/questionnaire",
            json=data,
            headers=headers
        )
        assert response.status_code == 400

    # возраст больше 119
    def test_questionnaire_age_too_high(self, api_client, base_url, new_registered_user):
        token = new_registered_user.token
        headers = {"Authorization": f"Bearer {token}"}
        
        data = {
            "first_name": new_registered_user.first_name,
            "last_name": new_registered_user.last_name,
            "age": 150,
            "city": new_registered_user.city,
            "bio": new_registered_user.bio or "Тест"
        }
        response = api_client.post(
            f"{base_url}/api/questionnaire",
            json=data,
            headers=headers
        )
        assert response.status_code == 400

    # возраст 120
    def test_questionnaire_age_120(self, api_client, base_url, new_registered_user):
        token = new_registered_user.token
        headers = {"Authorization": f"Bearer {token}"}
        
        data = {
            "first_name": new_registered_user.first_name,
            "last_name": new_registered_user.last_name,
            "age": 120,
            "city": new_registered_user.city,
            "bio": new_registered_user.bio or "Тест"
        }
        response = api_client.post(
            f"{base_url}/api/questionnaire",
            json=data,
            headers=headers
        )
        assert response.status_code == 400

    # возраст строкой
    def test_questionnaire_age_string(self, api_client, base_url, new_registered_user):
        token = new_registered_user.token
        headers = {"Authorization": f"Bearer {token}"}
        
        data = {
            "first_name": new_registered_user.first_name,
            "last_name": new_registered_user.last_name,
            "age": "двадцать пять",
            "city": new_registered_user.city,
            "bio": new_registered_user.bio or "Тест"
        }
        response = api_client.post(
            f"{base_url}/api/questionnaire",
            json=data,
            headers=headers
        )
        assert response.status_code == 400

    # очень длинное имя
    def test_questionnaire_very_long_first_name(self, api_client, base_url, new_registered_user):
        token = new_registered_user.token
        headers = {"Authorization": f"Bearer {token}"}
        
        data = {
            "first_name": "A" * 300,
            "last_name": new_registered_user.last_name,
            "age": 25,
            "city": new_registered_user.city,
            "bio": new_registered_user.bio or "Тест"
        }
        response = api_client.post(
            f"{base_url}/api/questionnaire",
            json=data,
            headers=headers
        )
        assert response.status_code in [400, 201]

    # xss в имени
    def test_questionnaire_xss_in_first_name(self, api_client, base_url, new_registered_user):
        token = new_registered_user.token
        headers = {"Authorization": f"Bearer {token}"}
        
        data = {
            "first_name": "<script>alert('xss')</script>",
            "last_name": new_registered_user.last_name,
            "age": 25,
            "city": new_registered_user.city,
            "bio": new_registered_user.bio or "Тест"
        }
        response = api_client.post(
            f"{base_url}/api/questionnaire",
            json=data,
            headers=headers
        )
        assert response.status_code in [201, 400]
        
        if response.status_code == 201:
            assert "<script>" not in response.json()["first_name"]

    # xss в bio
    def test_questionnaire_xss_in_bio(self, api_client, base_url, new_registered_user):
        token = new_registered_user.token
        headers = {"Authorization": f"Bearer {token}"}
        
        data = {
            "first_name": new_registered_user.first_name,
            "last_name": new_registered_user.last_name,
            "age": 25,
            "city": new_registered_user.city,
            "bio": "<img src='x' onerror='alert(1)'>"
        }
        response = api_client.post(
            f"{base_url}/api/questionnaire",
            json=data,
            headers=headers
        )
        assert response.status_code in [201, 400]
        
        if response.status_code == 201:
            assert "<img" not in response.json()["bio"]

    # спецсимволы
    def test_questionnaire_special_characters(self, api_client, base_url, new_registered_user):
        token = new_registered_user.token
        headers = {"Authorization": f"Bearer {token}"}
        
        data = {
            "first_name": "!@#$%^&*()",
            "last_name": new_registered_user.last_name,
            "age": 25,
            "city": new_registered_user.city,
            "bio": new_registered_user.bio or "Тест"
        }
        response = api_client.post(
            f"{base_url}/api/questionnaire",
            json=data,
            headers=headers
        )
        assert response.status_code in [201, 400]