def digit_of_life(date):
    while len(date) > 1:
        date = str(sum(int(digit) for digit in date))
    return int(date)

user_input = input("Enter your birthday (in any format like YYYYMMDD): ").strip()

if user_input.isdigit() and len(user_input) >= 1:
    result = digit_of_life(user_input)
    print(result)
else:
    print("Invalid input. Please enter digits only.")