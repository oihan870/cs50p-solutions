def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):

    # 1. longitud
    if len(s) < 2 or len(s) > 6:
        return False

    # 2. primeras dos letras
    if not s[0].isalpha() or not s[1].isalpha():
        return False

    # 3. solo letras y números
    if not s.isalnum():
        return False

    # 4. números no en medio
    number_started = False

    for char in s:
        if char.isdigit():

            if not number_started:
                number_started = True

                if char == "0":
                    return False
            else:
                if char < "0":
                    return False
        else:
            if number_started:
                return False

    return True


if __name__ == "__main__":
    main()
