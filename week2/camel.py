camel = input("camelCase: ")

snake = ""

for letter in camel:
    if letter.isupper():
        snake = snake + "_" + letter.lower()
    else:
        snake = snake + letter

print(snake)
