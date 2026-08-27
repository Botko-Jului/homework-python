import pytest


class TestAuthVerifyNegative:

    # неверный код
    def test_verify_wrong_code(self, api_client, base_url, new_user_data):
        api_client.post(
            f"{base_url}/api/auth/request-code",
            json={"email": new_user_data.email}
        )
        response = api_client.post(
            f"{base_url}/api/auth/verify",
            json={"email": new_user_data.email, "code": "000000"}
        )
        assert response.status_code == 400

    # пустой код
    def test_verify_empty_code(self, api_client, base_url, new_user_data):
        api_client.post(
            f"{base_url}/api/auth/request-code",
            json={"email": new_user_data.email}
        )
        response = api_client.post(
            f"{base_url}/api/auth/verify",
            json={"email": new_user_data.email, "code": ""}
        )
        assert response.status_code == 400

    # код с пробелом
    def test_verify_code_with_spaces(self, api_client, base_url, new_user_data):
        api_client.post(
            f"{base_url}/api/auth/request-code",
            json={"email": new_user_data.email}
        )
        response = api_client.post(
            f"{base_url}/api/auth/verify",
            json={"email": new_user_data.email, "code": "  123  "}
        )
        assert response.status_code == 400

    # чужой код
    def test_verify_code_for_another_email(self, api_client, base_url):
        response = api_client.post(
            f"{base_url}/api/auth/request-code",
            json={"email": "test1@example.com"}
        )
        code = response.json()["code"]
        
        response = api_client.post(
            f"{base_url}/api/auth/verify",
            json={"email": "test2@example.com", "code": code}
        )
        assert response.status_code == 400

    # пустой email
    def test_verify_empty_email(self, api_client, base_url, new_user_data):
        response = api_client.post(
            f"{base_url}/api/auth/request-code",
            json={"email": new_user_data.email}
        )
        code = response.json()["code"]
        
        response = api_client.post(
            f"{base_url}/api/auth/verify",
            json={"email": "", "code": code}
        )
        assert response.status_code == 400

    # email с пробелами
    def test_verify_email_with_spaces(self, api_client, base_url, new_user_data):
        response = api_client.post(
            f"{base_url}/api/auth/request-code",
            json={"email": new_user_data.email}
        )
        code = response.json()["code"]
        
        response = api_client.post(
            f"{base_url}/api/auth/verify",
            json={"email": "  test@example.com  ", "code": code}
        )
        assert response.status_code == 400

    # email как int
    def test_verify_int_email(self, api_client, base_url):
        response = api_client.post(
            f"{base_url}/api/auth/verify",
            json={"email": 12345, "code": "123456"}
        )
        assert response.status_code in [400, 500]

    # отсутствует email
    def test_verify_missing_email(self, api_client, base_url):
        response = api_client.post(
            f"{base_url}/api/auth/verify",
            json={"code": "123456"}
        )
        assert response.status_code == 400

    # отсутствует код
    def test_verify_missing_code(self, api_client, base_url, new_user_data):
        response = api_client.post(
            f"{base_url}/api/auth/verify",
            json={"email": new_user_data.email}
        )
        assert response.status_code == 400

    # пустое тело запроса
    def test_verify_empty_body(self, api_client, base_url):
        response = api_client.post(
            f"{base_url}/api/auth/verify",
            json={}
        )
        assert response.status_code == 400

    # лишние поля
    def test_verify_with_extra_fields(self, api_client, base_url, new_user_data):
        response = api_client.post(
            f"{base_url}/api/auth/request-code",
            json={"email": new_user_data.email}
        )
        code = response.json()["code"]
        
        response = api_client.post(
            f"{base_url}/api/auth/verify",
            json={
                "email": new_user_data.email,
                "code": code,
                "admin": True,
                "role": "superuser"
            }
        )
        assert response.status_code == 200

    # sql инъекция в email
    def test_verify_sql_injection_in_email(self, api_client, base_url):
        response = api_client.post(
            f"{base_url}/api/auth/verify",
            json={"email": "test@example.com' OR '1'='1", "code": "123456"}
        )
        assert response.status_code == 400

    # sql инъекция в код
    def test_verify_sql_injection_in_code(self, api_client, base_url, new_user_data):
        api_client.post(
            f"{base_url}/api/auth/request-code",
            json={"email": new_user_data.email}
        )
        response = api_client.post(
            f"{base_url}/api/auth/verify",
            json={"email": new_user_data.email, "code": "123' OR '1'='1"}
        )
        assert response.status_code == 400