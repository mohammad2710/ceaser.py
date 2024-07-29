

def caesar_cipher(text, shift):
    result = ""
    
    for char in text:
        if char.isalpha():
            ascii_offset = ord('A') if char.isupper() else ord('a')
            shifted_char = chr((ord(char) - ascii_offset + shift) % 26 + ascii_offset)
            result += shifted_char
        else:
            result += char
            
    return result

def caesar_decipher(text, shift):
    return caesar_cipher(text, -shift)

def main():
    choice = int(input("ادخل 1 للتشفير و 2 لفك التشفير: "))
    text = input("Enter the text: ")
    shift = int(input("Enter the shift value: "))
    
    if choice == 1:
        encrypted_text = caesar_cipher(text, shift)
        print("THIS IS ENCODE TXT:", encrypted_text)
    elif choice == 2:
        decrypted_text = caesar_decipher(text, shift)
        print("Decrypted:", decrypted_text)
    else:
        print("go to mama an cry")

if __name__ == "__main__":
    main()
