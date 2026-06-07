def shorten(word):
    result = ""

    for letter in word:
        if letter.lower() not in "aeiou":
             result += letter

    return result

def main():
    texto = input("Input: ")
    print(shorten(texto))

if __name__=="__main__":
    main()
