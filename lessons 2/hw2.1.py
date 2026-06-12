# 1
print("1. Квадрат числа")
number_1 = int(input("Введіть число: "))
number_pow = number_1 ** 2
print(f"Квадрат числа: {number_pow}")

print("")

# 2
print("2. Середнє трьох чисел")
number1_2 = int(input("Введіть перше число: "))
number2_2 = int(input("Введіть друге число: "))
number3_2 = int(input("Введіть третє число: "))

average_2 = (number1_2 + number2_2 + number3_2) / 3
print(f"Середнє: {average_2}")

print("")

# 3
print("3. Перетворення хвилин у години")
number_3 = int(input("Введіть кількість хвилин: "))

hour_3 = number_3 // 60
minute_3 = number_3 % 60

print(hour_3, "години", minute_3, "хвилин")

print("")

# 4
print("4. Розрахунок знижки")
price_4 = float(input("Введіть ціну: "))
discount_4 = float(input("Введіть знижку (%): "))

sales_4 = price_4 * discount_4 / 100
final_4 = price_4 - sales_4

print(f"Ціна зі знижкою: {final_4}")

print("")

# 5
print("5. Остання цифра числа")
number_5 = int(input("Введіть число: "))

last_5 = number_5 % 10

print(f"Остання цифра: {last_5}")

print("")

# 6
print("6. Периметр прямокутника")
length_6 = int(input("Введіть довжину: "))
width_6 = int(input("Введіть ширину: "))

perimeter_6 = (length_6 + width_6) * 2

print(f"Периметр: {perimeter_6}")

print("")

# 7
print("7. Виведення числа в стовпчик")
number_7 = int(input("Введіть 4-х значне число: "))

n1_7, number_7 = divmod(number_7, 1000)
n2_7, number_7 = divmod(number_7, 100)
n3_7, n4_7 = divmod(number_7, 10)

print(n1_7)
print(n2_7)
print(n3_7)
print(n4_7)