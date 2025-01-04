DIGIT_PATTERNS = {
    '0': [
        "#####",
        "#   #",
        "#   #",
        "#   #",
        "#   #",
        "#   #",
        "#####"
    ],
    '1': [
        "   #",
        "   #",
        "   #",
        "   #",
        "   #",
        "   #",
        "   #"
    ],
    '2': [
        "####",
        "   #",
        "   #",
        "####",
        "#   ",
        "#   ",
        "####"
    ],
    '3': [
        "####",
        "   #",
        "   #",
        "####",
        "   #",
        "   #",
        "####"
    ],
    '4': [
        "#  #",
        "#  #",
        "#  #",
        "####",
        "   #",
        "   #",
        "   #",
    ],
    '5': [
        "####",
        "#   ",
        "#   ",
        "####",
        "   #",
        "   #",
        "####"
    ],
    '6': [
        "####",
        "#   ",
        "#   ",
        "####",
        "#  #",
        "#  #",
        "####"
    ],
    '7': [
        "####",
        "   #",
        "   #",
        "   #",
        "   #",
        "   #",
        "   #"
    ],
    '8': [
        "####",
        "#  #",
        "#  #",
        "####",
        "#  #",
        "#  #",
        "####"
    ],
    '9': [
        "####",
        "#  #",
        "#  #",
        "####",
        "   #",
        "   #",
        "####"
    ]
}

def display_number(number):
    """Displays a number using the seven-segment patterns."""
    number_str = str(number)  # Convert the number to a string
    lines = [""] * 7  # Prepare 7 lines for the output

    # Build each line for the seven-segment display
    for digit in number_str:
        pattern = DIGIT_PATTERNS[digit]  # Get the pattern for the digit
        for i in range(7):
            lines[i] += pattern[i] + "  "  # Add the pattern and spacing

    # Print the completed lines
    for line in lines:
        print(line)


num = int(input("Enter a Integer Number: "))
# Display the number using the seven-segment display
display_number(num)