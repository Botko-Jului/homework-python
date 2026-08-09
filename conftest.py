import pytest


@pytest.fixture
def users():
    # фикстура
    return [
        {"name": "Alice", "age": 25},
        {"name": "Bob", "age": 18},
        {"name": "Charlie", "age": 17},
        {"name": "Diana", "age": 30},
        {"name": "Eve", "age": 16},
        {"name": "Frank", "age": 21},
        {"name": "Grace", "age": 12},
    ]


@pytest.fixture
def empty_users():
    # фикстура с пустым списком
    return []