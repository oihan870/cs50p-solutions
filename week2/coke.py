amount_due = 50

while amount_due > 0:

    coin = int(input("Insert your coin: "))

    if coin in [25,10,5]:
        amount_due -= coin

    if amount_due > 0:
        print("Amount Due:", amount_due)


print("Change Owed:", abs(amount_due))
print("Enjoy your soda!")
