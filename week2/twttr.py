text = input("Insert your text: ")

results = ""

for letter in text:
    if letter.lower() not in ["a","e","i","o","u"]:
        results += letter

print(results)

