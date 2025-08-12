#!/usr/bin/env python3
"""
Caesar Cipher Encryption & Decryption
--------------------------------------
Author: Rif (Internship Task)
Description:
    This script implements the Caesar Cipher algorithm for encrypting
    and decrypting text messages. It allows the user to:
      - Enter a message
      - Choose a shift value (integer)
      - Encrypt or decrypt the message
"""

def caesar_cipher(text: str, shift: int, mode: str) -> str:
    """
    Encrypts or decrypts a text using Caesar Cipher.

    Args:
        text (str): The input message to encrypt or decrypt.
        shift (int): The number of positions to shift each letter.
        mode (str): 'encrypt' or 'decrypt'.

    Returns:
        str: The resulting encrypted or decrypted text.
    """
    result = []
    # Adjust shift for decryption
    if mode.lower() == 'decrypt':
        shift = -shift

    for char in text:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            # Shift within alphabet range
            shifted_char = chr((ord(char) - base + shift) % 26 + base)
            result.append(shifted_char)
        else:
            # Non-alphabetical characters remain unchanged
            result.append(char)

    return ''.join(result)


def get_valid_int(prompt: str) -> int:
    """Prompt user for a valid integer input."""
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("❌ Please enter a valid integer.")


def main():
    print("=== Caesar Cipher Tool ===")
    message = input("Enter your message: ").strip()
    shift = get_valid_int("Enter shift value (integer): ")

    while True:
        mode = input("Choose mode (encrypt/decrypt): ").strip().lower()
        if mode in ('encrypt', 'decrypt'):
            break
        print("❌ Invalid mode. Please type 'encrypt' or 'decrypt'.")

    output = caesar_cipher(message, shift, mode)
    print(f"\nResult ({mode}ed text): {output}")


if __name__ == "__main__":
    main()

