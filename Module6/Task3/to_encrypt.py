def caesar_cipher(text, shift):
    encrypted_text = []
    for char in text:
        if char.isalpha():
            base = ord('a') if char.islower() else ord('A')
            encrypted_char = chr((ord(char) - base + shift) % 26 + base)
            encrypted_text.append(encrypted_char)
        else:
            encrypted_text.append(char)
    return ''.join(encrypted_text)

def get_valid_shift(prompt):
    while True:
        try:
            shift = int(input(prompt))
            if 1 <= shift <= 25:
                return shift
            else:
                print("Error: the shift value must be in the range 1..25.")
        except ValueError:
            print("Error: invalid input. Please enter an integer.")

text_to_encrypt = input("Enter the text to encrypt: ")
shift_value = get_valid_shift("Enter the shift value (1-25): ")
encrypted_text = caesar_cipher(text_to_encrypt, shift_value)
print("Encoded text:", encrypted_text)
