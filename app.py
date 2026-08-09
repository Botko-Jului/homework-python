def is_even(number):
    # Возвращает True, если число четное
    return number % 2 == 0


def is_palindrome(text):
    # Возвращает True, если строка читается одинаково слева направо и справа налево (без учёта регистра)
    if not isinstance(text, str):
        return False
    # Приводим к нижнему регистру и удаляем пробелы для корректной проверки
    cleaned = text.lower().replace(" ", "")
    return cleaned == cleaned[::-1]

def find_max(numbers):
    # Возвращает наибольшее число из списка без использования max()
    if not numbers:
        raise ValueError("Список не может быть пустым")
    
    max_number = numbers[0]
    for num in numbers:
        if num > max_number:
            max_number = num
    return max_number

def get_adult_users(users):
    # Из списка словарей, возвращаем только совершенолетних
     return [user for user in users if user["age"] >= 18]