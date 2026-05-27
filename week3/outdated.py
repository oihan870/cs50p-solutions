months = [
    "January", "February", "March", "April",
    "May", "June", "July", "August",
    "September", "October", "November", "December"
]

while True:
    try:
        date = input()

        # CASO 1: formato 9/8/1636
        if "/" in date:
            month, day, year = date.split("/")

            month = int(month)
            day = int(day)
            year = int(year)

        # CASO 2: formato September 8, 1636
        else:
            month_day, year = date.split(", ")
            month_name, day = month_day.split(" ")
            year = int(year)
            day = int(day)

            if month_name in months:
                month = months.index(month_name) + 1
            else:
                continue

        # validación básica
        if not (1 <= month <= 12 and 1 <= day <= 31):
            continue

        print(f"{year}-{month:02d}-{day:02d}")
        break

    except:
        continue
