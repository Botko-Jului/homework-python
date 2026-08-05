import pytest
import sys
import os

# Добавляем корневую папку проекта в путь поиска
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from app import is_even, is_palindrome


# Классы эквивалентности для is_even:
#    - Четные числа - true
#    - Нечетные числа - false

def test_is_even_positive_even():
    #четные числа - true
    assert is_even(4) is True
    assert is_even(100) is True 


def test_is_even_positive_odd():
    #нечетные числа - false
    assert is_even(5) is False
    assert is_even(99) is False  


# Граничные значения для is_even:

def test_is_even_boundary_zero():
    #0 (четное)
    assert is_even(0) is True


def test_is_even_boundary_negative_even():
    #-2 (отрицательное четное)
    assert is_even(-2) is True


def test_is_even_boundary_negative_odd():
     #-1 (отрицательное нечетное)
    assert is_even(-1) is False


# Дополнительный граничный тест
def test_is_even_boundary_between_0_and_1():
    #границa между 0 и 1
    assert is_even(0) is True
    assert is_even(1) is False

def test_is_even_large_number():
    # проверка большого чётного числа
    assert is_even(1000000) is True


# Тесты для is_palindrome 

# Классы эквивалентности для is_palindrome:
#    - Палиндромы - true
#    - Не палиндромы - false

def test_is_palindrome_valid_palindrome():
    assert is_palindrome("level") is True
    assert is_palindrome("radar") is True  


def test_is_palindrome_not_palindrome():
    assert is_palindrome("hello") is False
    assert is_palindrome("world") is False  

#  Граничные значения для is_palindrome:

def test_is_palindrome_boundary_empty():
    # пустая строка (0 символов)
    assert is_palindrome("") is True


def test_is_palindrome_boundary_one_char():
    # 1 символ (минимальный палиндром)
    assert is_palindrome("a") is True
    assert is_palindrome("Z") is True 


def test_is_palindrome_boundary_two_chars_palindrome():
   # 2 символа (палиндром)
    assert is_palindrome("aa") is True


def test_is_palindrome_boundary_two_chars_not_palindrome():
    # 2 символа (не палиндром)
    assert is_palindrome("ab") is False

#    - С учетом регистра
#    - С пробелами

def test_is_palindrome_case_insensitive():
    # палиндром с разным регистром
    assert is_palindrome("Able was I ere I saw Elba") is True


def test_is_palindrome_with_spaces():
    #палиндром с пробелами
    assert is_palindrome("never odd or even") is True


def test_is_palindrome_mixed_case_and_spaces():
    # регистр + пробелы
    assert is_palindrome("A man a plan a canal Panama") is True

def test_is_palindrome_number_as_string():
   # строки с числами-палиндромом
    assert is_palindrome("12321") is True

def test_is_palindrome_not_string():
   # нестроковое значением
    assert is_palindrome(12321) is False