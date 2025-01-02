import datetime
import os
import time

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
        "#",
        "#",
        "#",
        "#",
        "#",
        "#",
        "#"
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
    ],
    ':': [
        "    ",
        "    ",
        " ## ",
        "    ",
        " ## ",
        "    ",
        "    "
    ]
}

def display_time_in_digital_clock_style(time_string):
    """Display the given time string in a digital clock style."""
    lines = [""] * 7
    for char in time_string:
        pattern = DIGIT_PATTERNS[char]
        for i in range(7):
            lines[i] += pattern[i] + "  "

    for line in lines:
        print(line)

while True:
    now = datetime.datetime.now()
    today = datetime.date.today()

    current_time = now.strftime("%H:%M:%S")
    current_date = today.strftime("%Y-%m-%d")
    os.system('clear')

    # Display the current date and time
    print(f"Current Date: {current_date}")
    print("Current Time:")
    display_time_in_digital_clock_style(current_time)

    time.sleep(1)
