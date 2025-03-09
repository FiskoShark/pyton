# --------------------------------
# ------------- 1 ---------------
name = input("введіть ваше ім'я: ")
try:
    age = int(input("введіть ваш вік "))
    if age < 0 or age > 130:
        raise ValueError

    print(f"привіт, {name}! тобі — {age} років!\n")

except ValueError:
    print("Помилка: вік має бути в межах 0-130 років!\n")
# ------------- 1 ----------------
# --------------------------------
# ------------- 2.1 --------------
def greet_user(name, age):
    return f"привіт, {name}! тобі — {age} років!\n"

name = input("введіть ваше ім'я: ")

try:
    age = int(input("введіть ваш вік: "))
    if age < 0 or age > 130:
        raise ValueError

    print(greet_user(name, age))
except ValueError:
    print("Помилка: вік має бути в межах 0-130 років!\n")
# ------------- 2.1 ---------------
# ---------------------------------
# ------------- 2.2 ---------------
def greet_user_safe(name, age):
    if not (0 <= age <= 130):
        raise ValueError()
    return f"привіт, {name}! тобі — {age} років!\n"
name = input("введіть ваше ім'я: ")

try:
    age = int(input("введіть ваш вік: "))
    print(greet_user_safe(name, age))
except ValueError:
    print("Помилка: вік було введено некоректно!\n")

# ------------- 2.2 ---------------
# ---------------------------------
# ------------- 3 -----------------
def main():

    numbers = []

    while True:
        try:
            number = float(input("впишіть додатнє число (чи від'ємне для завершення): "))
            if number < 0:
                raise ValueError("введено НЕ додатне число, програма завершена")
            numbers.append(number)
        except ValueError as e:
            print(e)
            break

    if len(numbers) > 0:
        total = sum(numbers)
        print(f"сума всіх чисел - {total}\n")
    else:
        print("не було введено жодного числа\n")


if __name__ == "__main__":
    main()
# ------------- 3 -----------------
# ---------------------------------
# ------------- 4 -----------------
def sum_numbers(numbers):
    total = sum(numbers)
    return total


def main():
    numbers = []

    while True:
        try:
            number = float(input("впишіть додатнє число (чи від'ємне для завершення): "))
            if number < 0:
                raise ValueError("введено НЕ додатне число, програма завершена")
            numbers.append(number)
        except ValueError as e:
            print(e)
            break

    try:
        total = sum_numbers(numbers)
        print(f"сума всіх чисел - {total}")
    except Exception as e:
        print(f"сталася помилка - {e}")


if __name__ == "__main__":
    main()
# ------------- 4 ------------------
# ----------------------------------