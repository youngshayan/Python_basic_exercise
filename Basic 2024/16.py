def converter(year, month, day):
    if day >= 11  and 10 <= month <= 12:
        year += 622
        print(f"Your birthday is in {year}")
    else:
        year += 621
        print(f"Your birthday is in {year}")

day = int(input("Enter the day of your birthday: "))
month = int(input("Enter the month of your birthday: "))
year = int(input("Enter the year of your birthday: "))
converter(year, month, day)


