def is_even(number):
    """Возвращает True, если число четное."""
    return number % 2 == 0


def is_palindrome(text):
    """Возвращает True, если строка читается одинаково слева направо и справа налево (без учёта регистра)."""
    if not isinstance(text, str):
        return False
    # Приводим к нижнему регистру и удаляем пробелы для корректной проверки
    cleaned = text.lower().replace(" ", "")
    return cleaned == cleaned[::-1]