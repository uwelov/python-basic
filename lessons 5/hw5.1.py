import string
import keyword

name = "_"
# name = "__"
# name = "___"
# name = "x"
# name = "get_value"
# name = "get value"
# name = "get!value"
# name = "some_super_puper_value"
# name = "Get_value"
# name = "get_Value"
# name = "getValue"
# name = "3m"
# name = "m3"
# name = "assert"
# name = "assert_exception"

result = True

if len(name) == 0:
    result = False
elif name[0].isdigit():
    result = False
elif name in keyword.kwlist:
    result = False
elif "__" in name:
    result = False
else:
    for symbol in name:
        if symbol.isupper():
            result = False
            break

        if symbol == " ":
            result = False
            break

        if symbol in string.punctuation and symbol != "_":
            result = False
            break

print(f'{name} => {result}')