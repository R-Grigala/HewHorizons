def is_in_text(word, combination):
    word = word.lower()
    combination = combination.lower()
    
    index = 0

    for char in combination:
        # Check if the current character matches the current character in the word
        if char == word[index]:
            index += 1
        # If all characters of the word are found, return True
        if index == len(word):
            return True
    
    return False

word = input("Enter the word: ").strip()
combination = input("Enter the combination of characters: ").strip()

if is_in_text(word, combination):
    print("Yes")
else:
    print("No")