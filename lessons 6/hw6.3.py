number = 999

while number > 9:
    temp_number = str(number)
    number = 1
    for char in temp_number:
        if char.isdigit():
            number *= int(char)
    print(number)