import pytest
import sys
import os

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from app import get_adult_users


def test_get_adult_users_only_adults(users):
    # Проверяет, что возвращаются только совершеннолетние (18+)
    
    # Act - вызов функции
    result = get_adult_users(users)
    
    # Assert - проверка, что все пользователи 18+
    for user in result:
        assert user["age"] >= 18


def test_get_adult_users_age_18_included(users):
    # Проверяет, что пользователь с возрастом 18 лет включен в результат 
  
    expected_names = ["Alice", "Bob", "Diana", "Frank"]
    
    # Act
    result = get_adult_users(users)
    
    # Assert
    result_names = [user["name"] for user in result]
    assert "Bob" in result_names  
    assert "Alice" in result_names  
    assert "Diana" in result_names  
    assert "Frank" in result_names  


def test_get_adult_users_minors_excluded(users):
    # Проверяет, что несовершеннолетние (младше 18) не включены в результат

    # Arrange
    excluded_names = ["Charlie", "Eve", "Grace"]
    
    # Act
    result = get_adult_users(users)
    
    # Assert
    result_names = [user["name"] for user in result]
    for name in excluded_names:
        assert name not in result_names


def test_get_adult_users_count_correct(users):
    # Проверяет, что количество взрослых соответствует ожидаемому

    # Arrange
    expected_count = 4  # Alice(25), Bob(18), Diana(30), Frank(21)
    
    # Act
    result = get_adult_users(users)
    
    # Assert
    assert len(result) == expected_count


def test_get_adult_users_all_adults():
    # Проверяет, что если все пользователи взрослые, все возвращаются
    # Arrange
    all_adults = [
        {"name": "John", "age": 20},
        {"name": "Jane", "age": 25},
        {"name": "Jack", "age": 30},
    ]
    
    # Act
    result = get_adult_users(all_adults)
    
    # Assert
    assert len(result) == 3
    assert all(user["age"] >= 18 for user in result)


def test_get_adult_users_all_minors():
    # Проверяет, что если все пользователи несовершеннолетние, результат пустой
    # Arrange
    all_minors = [
        {"name": "Tom", "age": 10},
        {"name": "Jerry", "age": 15},
        {"name": "Spike", "age": 17},
    ]
    
    # Act
    result = get_adult_users(all_minors)
    
    # Assert
    assert result == []


def test_get_adult_users_empty(empty_users):
   # Проверяет, что при пустом списке возвращается пустой список 
    # Arrange - (фикстура empty_users уже подготовлена)
    
    # Act
    result = get_adult_users(empty_users)
    
    # Assert
    assert result == []