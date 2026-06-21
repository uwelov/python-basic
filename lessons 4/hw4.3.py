import random

numbers = []
numbers_size = random.randint(3, 10)

for i in range(numbers_size):
    numbers.append(random.randint(1, 10))

new_numbers = [numbers[0], numbers[2], numbers[-2]]
print(f"{numbers} == {new_numbers}")