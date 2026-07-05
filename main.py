def encrypt(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            start = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - start + shift) % 26 + start)
        else:
            result += char
    return result

def decrypt(text, shift):
    return encrypt(text, -shift)

while True:
    print("\n===== Caesar Cipher =====")
    print("1. Encrypt")
    print("2. Decrypt")
    print("3. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        text = input("Enter text: ")
        shift = int(input("Enter shift key: "))
        print("Encrypted Text:", encrypt(text, shift))

    elif choice == "2":
        text = input("Enter encrypted text: ")
        shift = int(input("Enter shift key: "))
        print("Decrypted Text:", decrypt(text, shift))

    elif choice == "3":
        print("Thank you!")
        break

    else:
        print("Invalid choice! Please try again.")