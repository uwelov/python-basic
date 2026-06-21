# numbers = [0, 1, 0, 12, 3]
# numbers = [0]
# numbers = [1, 0, 13, 0, 0, 0, 5]
numbers = [9, 0, 7, 31, 0, 45, 0, 45, 0, 45, 0, 0, 96, 0]
old_numbers = numbers.copy()
result = []

for i in numbers:
    if i != 0:
        result.append(i)

for i in numbers:
    if i == 0:
        result.append(i)

numbers = result.copy()
print(f"{old_numbers} -> {numbers}")