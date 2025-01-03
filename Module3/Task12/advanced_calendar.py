user_input = input("Enter a month and year in MM-YYYY format: ")

month, year = map(int, user_input.split("-"))

if month < 1 or month > 12 or year < 1:
    print("Invalid input. Please enter a valid month (1-12) and year.")
else:
    months = [
        "January", "February", "March", "April", "May", "June",
        "July", "August", "September", "October", "November", "December"
    ]
    days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    # Adjust for leap year
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        days_in_month[1] = 29

    weekdays = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]

    q = 1
    m = month
    y = year
    if m in [1, 2]:
        m += 12
        y -= 1

    h = (q + (13 * (m + 1)) // 5 + y + (y // 4) - (y // 100) + (y // 400)) % 7
    first_weekday = (h + 5) % 7  # Convert to 0=Mon, ..., 6=Sun

    print(f"{months[month - 1]} {year}")
    print(" ".join(weekdays))

    calendar = ["    "] * first_weekday

    for day in range(1, days_in_month[month - 1] + 1):
        calendar.append(f"{day:2}  ")

    for i in range(0, len(calendar), 7):
        print("".join(calendar[i:i + 7]))
