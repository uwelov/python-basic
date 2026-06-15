numbers = [12, 3, 4, 10]
#numbers = [1]
#numbers = []
#numbers = [12, 3, 4, 10, 8]

old_numbers = numbers.copy()

if len(numbers) <= 1:
    print(f"{old_numbers} => {numbers}")
else:
    last_number = numbers.pop()
    numbers.insert(0,last_number)
    print(f"{old_numbers} => {numbers}")