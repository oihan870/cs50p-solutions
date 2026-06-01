import random

def numero_entero(promt):
    while True:
        try:
            numero = int(input(promt))
            if numero > 0:
                return numero
        except ValueError:
            continue

def main():
    range = numero_entero("Level: ")
    secreto = random.randint(1, range)

    while True:
        guess = numero_entero("Guess: ")

        if guess < secreto:
            print("Too small!")
        elif guess > secreto:
            print("Too large!")
        else:
            print("Just right!")
            break

main()
