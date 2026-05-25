def main():
    plate = input("What is your plate? ")
    if plate_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def plate_valid(text):

    # 1. longitud
    if len(text) < 2 or len(text) > 6:
        return False

    # 2. primeras 2 letras
    if not text[0].isalpha() or not text[1].isalpha():
        return False

    # 3. solo letras y números
    if not text.isalnum():
        return False

    number_started = False

    # 4. reglas de números
    for letter in text:

        if letter.isdigit():

            if not number_started:
                number_started = True

                if letter == "0":
                    return False

        else:
            if number_started:
                return False

    return True

main()
