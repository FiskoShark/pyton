import random

# Створення двох списків з випадковими цілими числами
list1 = [random.randint(1, 25) for _ in range(10)]
list2 = [random.randint(1, 25) for _ in range(10)]
print(f"Список 1: {list1}")
print(f"Список 2: {list2}")

comb_list = list1 + list2
print(f"Об'єднаний список: {comb_list}")

combined_list = list(set(comb_list))
print(f"Список без повторень: {combined_list}")

common_elements_list = list(set(list1) & set(list2))
print(f"Спільні елементи: {common_elements_list}")

unique_list = list((set(list1) ^ set(list2)))
print(f"Унікальні елементи обох списків: {unique_list}")

minmax_list = [min(list1), max(list1), min(list2), max(list2)]
print(f"Мінімальні та максимальні значення: {minmax_list}")
