def is_palindrome(text):
    cleaned_text = ''.join(text.lower().split())
    left, right = 0, len(cleaned_text) - 1

    while left < right:
        if cleaned_text[left] != cleaned_text[right]:
            return False
        left += 1
        right -= 1
    return True

user_input = input("Enter some text: ").strip()

if user_input and is_palindrome(user_input):
    print("It's a palindrome")
else:
    print("It's not a palindrome")