# Strings
string_text = "Hello, Python World! Let's learn string methods in Python."
number_string = "10271999"
mixed_string = "hello271999"
tab_string = "Hello\tPython"

# capitalize(): Converts the first character to upper case
print("capitalize():", string_text.capitalize())

# casefold(): Converts string into lower case
print("casefold():", string_text.casefold())

# center(): Returns a centered string
print("center():", string_text.center(50, '-'))

# count(): Returns the number of times a specified value occurs in a string
print("count():", string_text.count("l"))

# encode(): Returns an encoded version of the string
print("encode():", string_text.encode())

# endswith(): Returns true if the string ends with the specified value
print("endswith():", string_text.endswith("!"))

# expandtabs(): Sets the tab size of the string
print("expandtabs():", tab_string.expandtabs(10))

# find(): Searches the string for a specified value and returns the position
print("find():", string_text.find("Python"))

# format(): Formats specified values in a string
print("format():", "{} is {}".format("Python", "awesome"))

# format_map(): Formats specified values using a dictionary
data = {"lang": "Python", "adj": "great"}
print("format_map():", "{lang} is {adj}".format_map(data))

# index(): Searches the string for a specified value and returns the position
print("index():", string_text.index("Python"))

# isalnum(): Returns True if all characters are alphanumeric
print("isalnum():", mixed_string.isalnum())

# isalpha(): Returns True if all characters are in the alphabet
print("isalpha():", string_text.isalpha())

# isascii(): Returns True if all characters are ASCII
print("isascii():", string_text.isascii())

# isdecimal(): Returns True if all characters are decimals
print("isdecimal():", number_string.isdecimal())

# isdigit(): Returns True if all characters are digits
print("isdigit():", number_string.isdigit())

# isidentifier(): Returns True if the string is a valid identifier
print("isidentifier():", "variable_name".isidentifier())

# islower(): Returns True if all characters are lower case
print("islower():", string_text.islower())

# isnumeric(): Returns True if all characters are numeric
print("isnumeric():", number_string.isnumeric())

# isprintable(): Returns True if all characters are printable
print("isprintable():", string_text.isprintable())

# isspace(): Returns True if all characters are whitespaces
print("isspace():", "   ".isspace())

# istitle(): Returns True if the string follows the rules of a title
print("istitle():", string_text.istitle())

# isupper(): Returns True if all characters are upper case
print("isupper():", string_text.isupper())

# join(): Converts the elements of an iterable into a string
print("join():", "-".join(["Python", "is", "fun"]))

# ljust(): Returns a left justified version of the string
print("ljust():", string_text.ljust(50, '-'))

# lower(): Converts a string into lower case
print("lower():", string_text.lower())

# lstrip(): Returns a left trim version of the string
print("lstrip():", string_text.lstrip())

# maketrans() and translate(): Returns a translated string
trans_table = str.maketrans("aeiou", "12345")
print("translate():", string_text.translate(trans_table))

# partition(): Returns a tuple where the string is parted into three parts
print("partition():", string_text.partition("Python"))

# replace(): Returns a string where a specified value is replaced with a specified value
print("replace():", string_text.replace("Python", "Java"))

# rfind(): Searches the string for a specified value and returns the last position
print("rfind():", string_text.rfind("Python"))

# rindex(): Searches the string for a specified value and returns the last position
print("rindex():", string_text.rindex("Python"))

# rjust(): Returns a right justified version of the string
print("rjust():", string_text.rjust(50, '-'))

# rpartition(): Returns a tuple where the string is parted into three parts
print("rpartition():", string_text.rpartition("Python"))

# rsplit(): Splits the string at the specified separator, and returns a list
print("rsplit():", string_text.rsplit(" ", 2))

# rstrip(): Returns a right trim version of the string
print("rstrip():", string_text.rstrip())

# split(): Splits the string at the specified separator, and returns a list
print("split():", string_text.split())

# splitlines(): Splits the string at line breaks and returns a list
multi_line = "Hello\nWorld"
print("splitlines():", multi_line.splitlines())

# startswith(): Returns true if the string starts with the specified value
print("startswith():", string_text.startswith("Hello"))

# strip(): Returns a trimmed version of the string
print("strip():", string_text.strip())

# swapcase(): Swaps cases, lower case becomes upper case and vice versa
print("swapcase():", string_text.swapcase())

# title(): Converts the first character of each word to upper case
print("title():", string_text.title())

# upper(): Converts a string into upper case
print("upper():", string_text.upper())

# zfill(): Fills the string with a specified number of 0 values at the beginning
print("zfill():", number_string.zfill(10))