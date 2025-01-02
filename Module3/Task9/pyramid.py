blocks = int(input("Enter the number of blocks: "))

height = 0
used_blocks = 0

while used_blocks + (height + 1) <= blocks:
    height += 1
    used_blocks += height

# Output the result
print("The height of the pyramid:", height)