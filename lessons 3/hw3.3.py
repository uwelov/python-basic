numbers = [1, 2, 3, 4, 5, 6]
#numbers = [1, 2, 3]
#numbers = [1, 2, 3, 4, 5]
#numbers = [1]
#numbers = []

old_numbers = numbers.copy()

middle_index = len(numbers) // 2
if len(numbers) % 2 != 0:
    middle_index += 1

first_part = numbers[:middle_index]
second_part = numbers[middle_index:]

result = [first_part, second_part]
print(f"{old_numbers} => {result}")