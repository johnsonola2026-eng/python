from builtins import input, print

text = input("Enter text: ")

for character in text:
    if character.isalpha():
        print(f"{character!r} is an alphabet.")
    else:
     print(f"{character!r} is not an alphabet.")