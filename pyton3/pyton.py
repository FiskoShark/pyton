first_num = float(input("Введіть перше число: "))
operation = input("Введіть дію (+, -, *, /): ")
second_num = float(input("Введіть друге число: "))

if operation == "+":
    result = first_num + second_num
elif operation == "-":
    result = first_num - second_num
elif operation == "*":
    result = first_num * second_num
elif operation == "/":
    result = first_num / second_num
else:
    result = "Неправильна операція"
print(f"Результат: {result}")




import random

numbers = []
for i in range(20):
    numbers.append(random.randint(-10, 10))

print(f"Список чисел: {numbers}")
min_element = numbers[0]
max_element = numbers[0]

negative_count = 0
positive_count = 0
zero_count = 0

for num in numbers:
    if num < min_element:
        min_element = num
    if num > max_element:
        max_element = num
    if num < 0:
        negative_count += 1
    elif num > 0:
        positive_count += 1
    else:
        zero_count += 1

print(f"Мінімальний елемент: {min_element}")
print(f"Максимальний елемент: {max_element}")
print(f"Кількість від'ємних елементів: {negative_count}")
print(f"Кількість додатних елементів: {positive_count}")
print(f"Кількість нулів: {zero_count}")







