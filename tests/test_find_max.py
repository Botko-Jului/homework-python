import pytest
import sys
import os

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from app import find_max


# Параметризованные тесты (минимум 4 разных списка)
@pytest.mark.parametrize("numbers, expected", [
    # 1. Положительные числа
    ([1, 5, 3, 9, 2], 9),
    # 2. Отрицательные числа
    ([-5, -1, -10, -3], -1),
    # 3. Один элемент
    ([42], 42),
    # 4. Вперемешку (положительные, отрицательные, ноль)
    ([-10, 0, 5, -3, 8, -1], 8),
    # Одинаковые
    ([7, 7, 7, 7], 7)
])

def test_find_max(numbers, expected):

    # Act - вызов функции
    result = find_max(numbers)  
    # Assert - проверка результата
    assert result == expected


def test_find_max_empty_list():
    # Arrange - подготовка пустого списка
    empty_list = []
    
    # Act - вызов функции с пустым списком
    # Assert - проверка, что выбрасывается ValueError
    with pytest.raises(ValueError) as exc_info:
        find_max(empty_list)
    
    # Дополнительная проверка сообщения об ошибке
    assert str(exc_info.value) == "Список не может быть пустым"