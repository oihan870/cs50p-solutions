names = []

while True:
    try:
        names.append(input("Name: "))
    except EOFError:
        break

if len(names) == 1:
    print(f"\nAdieu, adieu, to {names[0]}")

elif len(names) == 2:
    print(f"\nAdieu, adieu, to {names[0]} and {names[1]}")

else:
    print("\nAdieu, adieu, to " + ", ".join(names[:-1]) + ", and " + names[-1])
