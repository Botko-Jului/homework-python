"""
Фикстура
"""


import pytest
import requests
import random
import string
import uuid
from typing import Dict, Any
from dataclasses import dataclass


# Конфигурация

BASE_URL = "http://localhost:5001"



# Класс для хранения данных пользователя


@dataclass
class UserData:
    email: str = ""
    first_name: str = ""
    last_name: str = ""
    age: int = 0
    city: str = ""
    bio: str = ""
    token: str = ""
    code: str = ""
    profile_completed: bool = False

    def to_dict(self) -> Dict[str, Any]:
       
        return {
            "email": self.email,
            "first_name": self.first_name,
            "last_name": self.last_name,
            "age": self.age,
            "city": self.city,
            "bio": self.bio
        }

    def to_questionnaire_dict(self) -> Dict[str, Any]:
    
        return {
            "first_name": self.first_name,
            "last_name": self.last_name,
            "age": self.age,
            "city": self.city,
            "bio": self.bio
        }

# Генерация тестовых данных


class DataGenerator:
    
    # Домены для тестирования разных почтовых сервисов
    DOMAINS = [
        "example.com",
        "mail.ru",
        "gmail.com",
        "yandex.ru",
        "company.co.uk",
        "test.io",
        "test.org",
        "test.net",
        "test.info",
    ]
    
    @staticmethod
    def generate_unique_email(domain: str = None) -> str:
        
        if domain is None:
            domain = random.choice(DataGenerator.DOMAINS)
        
        unique_part = uuid.uuid4().hex[:8]
        return f"test_{unique_part}@{domain}"
    
    @staticmethod
    def generate_invalid_emails() -> list:
        
        return [
            # Пустые и пробелы
            "",
            "   ",
            
            # Без @
            "testexample.com",
            "test.mail.ru",
            
            # Без локальной части
            "@example.com",
            "@mail.ru",
            
            # Без домена
            "test@",
            "test@.",
            
            # Нет точки в домене
            "test@example",
            "test@mailru",
            
            # С пробелами
            "test @example.com",
            "test@example .com",
            
            # Специальные символы в домене
            "test@exa!mple.com",
            "test@exa*mple.com",
            "test@exa mple.com",
            
            # Двойная точка
            "test@example..com",
            "test@mail..ru",
            
            # Точка в начале домена
            "test@.example.com",
            "test@.mail.ru",
            
            # Дефис в неправильном месте
            "test@-example.com",
            "test@example-.com",
            
            # Слишком длинный домен
            "test@example" + "a" * 100 + ".com",
        ]
    
    @staticmethod
    def generate_first_name() -> str:
        
        names = [
            "Иван", "Петр", "Алексей", "Мария", "Елена",
            "Анна", "Дмитрий", "Сергей", "Ольга", "Татьяна",
            "Николай", "Екатерина", "Александр", "Виктория"
        ]
        return random.choice(names)
    
    @staticmethod
    def generate_last_name() -> str:
        surnames = [
            "Иванов", "Петров", "Сидоров", "Смирнов", "Кузнецов",
            "Попов", "Васильев", "Федоров", "Михайлов", "Соколов",
            "Новиков", "Морозов", "Волков", "Алексеев", "Лебедев"
        ]
        return random.choice(surnames)
    
    @staticmethod
    def generate_age() -> int:
        return random.randint(1, 119)
    
    @staticmethod
    def generate_city() -> str:
        cities = [
            "Москва", "Санкт-Петербург", "Новосибирск", "Екатеринбург",
            "Казань", "Нижний Новгород", "Челябинск", "Омск",
            "Ростов-на-Дону", "Уфа", "Красноярск", "Воронеж",
            "Пермь", "Волгоград", "Краснодар"
        ]
        return random.choice(cities)
    
    @staticmethod
    def generate_bio() -> str:
    
        bios = [
            "Тестовый пользователь",
            "Любитель автоматизации тестирования",
            "QA инженер с опытом",
            "Разработчик на Python",
            "Студент факультета информатики",
            "Тестировщик-энтузиаст",
            "Автоматизатор с душой разработчика",
            "",  
            "   ",  
            "!@#$%^&*()",  
            "🥳",  
            "Тестик" * 100, 
            "<script>alert('xss')</script>",  # XSS попытка
        ]
        return random.choice(bios)
    
    @classmethod
    def create_user_data(cls, **kwargs) -> UserData:
        
        return UserData(
            email=kwargs.get('email', cls.generate_unique_email()),
            first_name=kwargs.get('first_name', cls.generate_first_name()),
            last_name=kwargs.get('last_name', cls.generate_last_name()),
            age=kwargs.get('age', cls.generate_age()),
            city=kwargs.get('city', cls.generate_city()),
            bio=kwargs.get('bio', cls.generate_bio())
        )
# Вспомогательные функции
def extract_code_from_response(response):
    return response.json().get("code")

# Базовые фикстуры 

@pytest.fixture(scope="session")
def base_url() -> str:
    return BASE_URL

@pytest.fixture(scope="function")
def api_client() -> requests.Session:
    session = requests.Session()
    session.headers.update({"Content-Type": "application/json"})
    return session

# Фикстура для авторизации

@pytest.fixture(scope="function")
def data_generator() -> DataGenerator:
    return DataGenerator()

@pytest.fixture(scope="function")
def new_user_data(data_generator) -> UserData:
    return data_generator.create_user_data()

@pytest.fixture(scope="function")
def new_registered_user(api_client, base_url, new_user_data) -> UserData:

    # Запрос кода
    response = api_client.post(
        f"{base_url}/api/auth/request-code",
        json={"email": new_user_data.email}
    )
    assert response.status_code == 200
    new_user_data.code = extract_code_from_response(response)
    
    # Проверка кода
    response = api_client.post(
        f"{base_url}/api/auth/verify",
        json={"email": new_user_data.email, "code": new_user_data.code}
    )
    assert response.status_code == 200
    new_user_data.token = response.json()["token"]
    new_user_data.profile_completed = response.json()["profile_completed"]
    
    return new_user_data

@pytest.fixture(scope="function")
def user_without_questionnaire(new_registered_user) -> UserData:
    return new_registered_user

@pytest.fixture(scope="function")
def full_user_data(api_client, base_url, new_registered_user) -> UserData:
    response = api_client.post(
        f"{base_url}/api/questionnaire",
        json=new_registered_user.to_questionnaire_dict(),
        headers={"Authorization": f"Bearer {new_registered_user.token}"}
    )
    assert response.status_code == 201, "Не удалось заполнить анкету"
    new_registered_user.profile_completed = True
    return new_registered_user

@pytest.fixture(scope="function")
def auth_api_client(api_client, new_registered_user) -> requests.Session:
    client = api_client
    client.headers.update({"Authorization": f"Bearer {new_registered_user.token}"})
    return client


# Параметризация для негативных тестов

@pytest.fixture(params=[
    "",  # пустой
    "   ",  # пробелы
    "testexample.com",  # без @
    "@example.com",  # без локальной части
    "test@",  # без домена
    "test@example",  # без точки
])
def invalid_email(request):
    return request.param

@pytest.fixture(params=[
    {"first_name": ""},
    {"last_name": ""},
    {"city": ""},
    {"age": 0},
    {"age": -5},
    {"age": 150},
    {"age": "twenty"},
])
def invalid_questionnaire_data(request):
    return request.param

@pytest.fixture(params=[
    "invalid_token",
    "",
    "   ",
    "12345",
    "Bearer invalid",
])
def invalid_token(request):
    return request.param

@pytest.fixture(scope="session")
def auth_data():
    return {"email": None, "code": None, "token": None}

# Подключаем плагин Playwright для UI-тестов
pytest_plugins = ['pytest_playwright']