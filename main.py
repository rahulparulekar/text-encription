# Define a function to encrypt a message using the Caesar cipher
def encrypt_caesar(plaintext, shift):
    encrypted_text = ""
    for char in plaintext:
        if char.isalpha():
            is_upper = char.isupper()  # Check if the character is uppercase
            char = char.lower()  # Convert character to lowercase for encryption
            encrypted_char = chr(((ord(char) - 97 + shift) % 26) + 97)
            if is_upper:
                encrypted_char = encrypted_char.upper()  # Convert back to uppercase if the original character was uppercase
            encrypted_text += encrypted_char
        else:
            encrypted_text += char  # Preserve non-alphabet characters

    return encrypted_text

# Define a function to decrypt a Caesar cipher message
def decrypt_caesar(ciphertext, shift):
    decrypted_text = ""
    for char in ciphertext:
        if char.isalpha():
            is_upper = char.isupper()
            char = char.lower()
            decrypted_char = chr(((ord(char) - 97 - shift) % 26) + 97)
            if is_upper:
                decrypted_char = decrypted_char.upper()
            decrypted_text += decrypted_char
        else:
            decrypted_text += char

    return decrypted_text

# Main program
if __name__ == "__main__":
    while True:
        choice = input("Choose an option:\n1. Encrypt\n2. Decrypt\n3. Quit\n")

        if choice == "1":
            plaintext = input("Enter the message to encrypt: ")
            shift = int(input("Enter the shift value (e.g., 3): "))
            encrypted_message = encrypt_caesar(plaintext, shift)
            print("Encrypted message:", encrypted_message)
        elif choice == "2":
            ciphertext = input("Enter the message to decrypt: ")
            shift = int(input("Enter the shift value (e.g., 3): "))
            decrypted_message = decrypt_caesar(ciphertext, shift)
            print("Decrypted message:", decrypted_message)
        elif choice == "3":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please choose 1, 2, or 3.")

# The program presents a menu to the user, allowing them to encrypt, decrypt, or quit.
# When encrypting or decrypting, it asks for the message and the shift value.
# The shift value determines how much each letter is shifted in the alphabet.
# It handles both uppercase and lowercase letters, preserving non-alphabet characters.
