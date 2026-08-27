import pytest


class TestProfileNegative:
    """Негативные тесты для получения профиля"""
    
    #  без токена

    def test_get_profile_without_token(self, api_client, base_url):
        response = api_client.get(
            f"{base_url}/api/profile"
        )
        assert response.status_code == 401

    # невалидный токен
    
    def test_get_profile_invalid_token(self, api_client, base_url, invalid_token):
        headers = {"Authorization": f"Bearer {invalid_token}"}
        response = api_client.get(
            f"{base_url}/api/profile",
            headers=headers
        )
        assert response.status_code == 401
    
    # Получение профиля с токеном содержащим пробелы

    def test_get_profile_token_with_spaces(self, api_client, base_url):
        headers = {"Authorization": "Bearer  123 456  "}
        response = api_client.get(
            f"{base_url}/api/profile",
            headers=headers
        )
        assert response.status_code == 401
    # Без Bearer

    def test_get_profile_wrong_token_format(self, api_client, base_url):
        headers = {"Authorization": "123456"}
        response = api_client.get(
            f"{base_url}/api/profile",
            headers=headers
        )
        assert response.status_code == 401

    

    # Анкета не заполнена у пользователя
    
    def test_get_profile_token_without_questionnaire(self, api_client, base_url, new_registered_user):
        
        token = new_registered_user.token
        headers = {"Authorization": f"Bearer {token}"}
        
        response = api_client.get(
            f"{base_url}/api/profile",
            headers=headers
        )
        assert response.status_code == 403