import string

user_input = input("Enter letters in format 'a-c': ")

letters = string.ascii_letters 
first_letter, second_letter = user_input.split("-")
start_index = letters.index(first_letter)
end_index = letters.index(second_letter)

result = letters[start_index:end_index + 1]
print(result)