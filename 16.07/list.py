#Задание 1 "Магазин"

#Словарь с товарами
products = {
    "apple": {"quantity": 10, "price": 100},
    "banana": {"quantity": 20, "price": 50},
    "orange": {"quantity": 15, "price": 80},
    "grape": {"quantity": 8, "price": 120},
    "milk": {"quantity": 12, "price": 90},
    "bread": {"quantity": 30, "price": 40}
}

#Увеличить цену на 20%
for product in products:
    products[product]["price"] *= 1.2

#Удалить молоко
del products["milk"]

# Добавляем Salt
products["salt"] = {"quantity": 7, "price": 12}

# Общая стоимость
total_cost = 0
for product, info in products.items():
    total_cost += info["quantity"] * info["price"]

print(total_cost)  

#Задание 2 "Alice"

#два списка одинаковой длины
keys = ['name', 'age', 'city', 'occupation', 'email', 'phone', 'hobby', 'education', 'company', 'salary']
values = ['Alice', 30, 'New York', 'Engineer', 'alice@example.com', '+1234567890', 'Reading', 'Masters in Computer Science', 'TechCorp', 90000]

#словарь из двух списков
info = {}
for i in range(len(keys)):
    info[keys[i]] = values[i]

#Выводим словарь на экран
print(info)


#Задание 3 "цифр"

#ключ к шифру 
cipher = {
    "а": "щ", "б": "д", "в": "ю", "г": "ф", "д": "з", "е": "м", "ё": "р",
    "ж": "т", "з": "п", "и": "я", "й": "с", "к": "н", "л": "э", "м": "к",
    "н": "л", "о": "ё", "п": "ж", "р": "ц", "с": "б", "т": "у", "у": "в",
    "ф": "о", "х": "и", "ц": "х", "ч": "г", "ш": "е", "щ": "й", "ъ": "ы",
    "ы": "ч", "ь": "ш", "э": "ъ", "ю": "а", "я": "ь"
}

#зашифрованное сообщение
message = "2__234йшDGмёшSDFжкъrrrщзнSDF78юкйфуSDFшёью$#2Sшжйи3%узфsdf34нкфыvvя"

#рассшифровка
result = ""
for simvol in message:
    # Проверяем, есть ли символ в словаре (как ключ)
    if simvol in cipher:
        result = result + cipher[simvol]

print("Расшифрованное сообщение:", result

#дополнительная программа:

cipher_naoborot = {}
for key, value in cipher.items():
    cipher_naoborot[value] = key

#ввод сообщения
text = input("Введите сообщение:")

#шифруем
encrypted = ""
for bukva in text:
    # Приводим к нижнему регистру, чтобы совпадало со словарем
    bukva = bukva.lower()
    
    if bukva in cipher_naoborot:
        encrypted = zencrypted + cipher_naoborot[bukva]
    else:
        # Если буквы нет в словаре - оставляем как есть
        encrypted = encrypted + bukva

print("Зашифрованное сообщение:", encrypted)

#Задание 4 "Самая популярная буква"

#диалог
dialog = """Doc: Запомни! Согласно моей теории, ты помешал знакомству своих родителей.
Если они не встретятся, то не влюбятся, не поженятся, и у них не будет детей.
Поэтому твой старший брат исчезает с фотографии. Затем очередь твоей сестры,
и если ты все не исправишь, ты будешь следующим.
Marty: Тяжелый случай.
Doc: Вес тут совершенно ни при чем. """

#пустой словарь для подсчета букв
count = {}

# Перебираем каждый символ в тексте
for char in dialog:
    # Приводим букву к нижнему регистру
    char = char.lower()
    
    # Проверяем, является ли символ буквой (русской или английской)
    if char.isalpha():
        # Если буква уже есть в словаре - увеличиваем счетчик
        if char in count:
            count[char] = count[char] + 1
        # Если буквы нет - добавляем её со значением 1
        else:
            count[char] = 1

#выводим словарь с подсчетом букв
print("Словарь с количеством букв:")
print(count)
print()

# Находим букву с максимальным количеством
max_letter = ""  # переменная для буквы
max_count = 0    # переменная для количества

for letter, number in count.items():
    if number > max_count:
        max_count = number
        max_letter = letter

# Выводим результат
print("Самая популярная буква:", max_letter)
print("Встречается раз:", max_count)

