#numbers = []
#numbers = [0, 1, 7, 2, 4, 8]
#numbers = [1, 3, 5]
numbers = [6]
result = 0

if numbers:
    for i in range(0, len(numbers), 2):
        result += numbers[i]
    result *= numbers[-1]

print(result)