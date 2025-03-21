# ------------- 1 ---------------------
num1 = float(input("введіть перше число "))
num2 = float(input("введіть друге число "))
num3 = float(input("введіть третє число "))
suma = num1 + num2 + num3
product_result = num1 * num2 * num3
print(f"сума чисел: {suma}")
print(f"добуток чисел: {product_result}")

# -------------- 2 --------------------

salary = float(input("введіть вашу місячну зарплату "))
payment = float(input("введіть суму платежу за місячним кредитом "))
utility_debt = float(input("введіть заборгованість за комунальні послуги "))

balance = salary - payment - utility_debt

if balance < 0:
    print("Пора гасити борг!")
print("Залишок після виплат:", balance)

# --------------- 3 -------------------

length = float(input("введіть довжину першої діагоналі ромба: "))
length1 = float(input("введіть довжину другої діагоналі ромба: "))

area = (length * length1) / 2
print(f"площа ромба: {area}")
# -------------------------------------
