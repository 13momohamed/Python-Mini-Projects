def vigenere(message, key, direction=1):
    key_index = 0
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    final_message = ''

    for char in message.lower():

        # Append any non-letter character to the message
        if not char.isalpha():
            final_message += char
        else:        
            # Find the right key character to encode/decode
            key_char = key[key_index % len(key)]
            key_index += 1

            # Define the offset and the encrypted/decrypted letter
            offset = alphabet.index(key_char)
            index = alphabet.find(char)
            new_index = (index + offset*direction) % len(alphabet)
            final_message += alphabet[new_index]
    
    return final_message

def encrypt(message, key):
    return "Encrpted message: " + vigenere(message, key)
    
def decrypt(message, key):
    return "Decrypted message: " + vigenere(message, key, -1)

text = input("Write down the code to be encrypted/decrypted. ")
custom_key = input("Write down the key.")

prompt = input("Do you want to encrypt or decrypt the message?")
prompt = prompt.lower()

if prompt == 'encrypt':
    print(encrypt(text, custom_key))
elif prompt == 'decrypt':
    print(decrypt(text, custom_key))
else:
    print("Invalid input.")