import string

text = input("Enter text: ")

hashtag = "#"
new_word = True

for symbol in text:
    if symbol == " " or symbol in string.punctuation:
        new_word = True
    else:
        if new_word:
            hashtag += symbol.upper()
            new_word = False
        else:
            hashtag += symbol.lower()

if len(hashtag) > 140:
    hashtag = hashtag[:140]

print(hashtag)