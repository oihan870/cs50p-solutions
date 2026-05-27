while True:

    try:
        fraction = input("Fraction: ")

        x, y = fraction.split("/")

        x = int(x)
        y = int(y)

        if x > y:
            continue

        result = x / y * 100

        break

    except (ValueError, ZeroDivisionError):
        continue


if result <= 1:
    print("E")
    print(f"{(result)}%")

elif result >= 99:
    print("F")
    print(f"{(result)}%")

else:
    print(f"{(result)}%")
