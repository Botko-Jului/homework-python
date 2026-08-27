import pytest


class TestQuestionnairePositive:
    
    def test_questionnaire_success(self, api_client, base_url, new_user_data, auth_data):
        
        # Берем токен из auth_data
        token = auth_data["token"]
        email = auth_data["email"]
        
        headers = {"Authorization": f"Bearer {token}"}
        
        questionnaire_data = {
            "first_name": new_user_data.first_name,
            "last_name": new_user_data.last_name,
            "age": new_user_data.age,
            "city": new_user_data.city,
            "bio": new_user_data.bio
        }
        
        response = api_client.post(
            f"{base_url}/api/questionnaire",
            json=questionnaire_data,
            headers=headers
        )
        
        assert response.status_code == 201
        data = response.json()
        assert data["email"] == email
        assert data["first_name"] == new_user_data.first_name
        assert data["last_name"] == new_user_data.last_name
        assert data["age"] == new_user_data.age
        assert data["city"] == new_user_data.city
        assert data["bio"] == new_user_data.bio
        
        print(f"\n✅ Анкета заполнена для: {email}")