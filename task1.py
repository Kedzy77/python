alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
letter_to_index = dict(zip(alphabet, range(len(alphabet))))
index_to_letter = dict(zip(range(len(alphabet)), alphabet))


def encrypt(message, key):
    message = message.upper()
    key = key.upper()

    encrypted = ""
    split_message = [message[i:i + len(key)] for i in range(0, len(message), len(key))]

    for each_split in split_message:
        i = 0
        for letter in each_split:
            if letter in alphabet:
                number = (letter_to_index[letter] + letter_to_index[key[i]]) % len(alphabet)
                encrypted += index_to_letter[number]
                i += 1
            else:
                encrypted += letter

    return encrypted


def decrypt(cipher, key):
    cipher = cipher.upper()
    key = key.upper()

    decrypted = ""
    split_encrypted = [cipher[i:i + len(key)] for i in range(0, len(cipher), len(key))]

    for each_split in split_encrypted:
        i = 0
        for letter in each_split:
            if letter in alphabet:
                number = (letter_to_index[letter] - letter_to_index[key[i]]) % len(alphabet)
                decrypted += index_to_letter[number]
                i += 1
            else:
                decrypted += letter

    return decrypted

def main():
    message = "CRYPTOGRAPH"
    key = "ZORK"

    encrypted_message = encrypt(message, key)
    decrypted_message = decrypt(encrypted_message, key)

    print("Original message: " + message)
    print("Encrypted message: " + encrypted_message)
    print("Decrypted message: " + decrypted_message)

if __name__ == "__main__":
    main()
