while True:
    number_1 = int(input("Enter a number: "))
    number_2 = int(input("Enter another number: "))
    symbol = input("Enter a symbol: ")

    if symbol == "/":
        if number_2 == 0:
            print("You can't divide by zero!")
        else:
            result = number_1 / number_2
            print(result)

    elif symbol == "*":
        result = number_1 * number_2
        print(result)

    elif symbol == "+":
        result = number_1 + number_2
        print(result)

    elif symbol == "-":
        result = number_1 - number_2
        print(result)

    else:
        print("Unknown symbol!")

    user_answer = input("Do you want to continue? Enter yes or y: ").lower()

    if user_answer != "yes" and user_answer != "y":
        print("Exit from calculator...")
        break