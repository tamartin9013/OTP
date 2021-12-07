import string
import random

text = string.ascii_lowercase
otp = list(text)

#Takes plaintext input and key input and outputs ciphertext
def encrypt(msg, key):
    ciphertext = ''
    for id, char in enumerate(msg):
        charId = text.index(char)
        keyId = otp.index(key[id])

        cipher = (keyId + charId) % len(otp)
        ciphertext += text[cipher]

    return ciphertext


#Takes ciphertext input and key input and outputs the plaintext
def decrypt(ciphertext, key):

    if ciphertext == '' or key == '':
        return ''

    charIdx = text.index(ciphertext[0])
    keyIdx = otp.index(key[0])

    cipher = (charIdx - keyIdx) % len(otp)
    char = text[cipher]

    plaintext = char + decrypt(ciphertext[1:], key[1:])
    return plaintext 
    

#Main function contains menu options to choose to encrypt or decrypt.
#When encryption is chosen, a random key is genrated.
#When decryption is chosen, the program asks for the decryption key from the user.
if __name__ == '__main__':
    menu = {}
    menu['1:']="Encrypt" 
    menu['2:']="Decrypt"

    
    msg = input("Message: ")

    while True: 
        options=menu.keys()
        for choice in options: 
            print(choice, menu[choice])

        selection = input("Select Option:") 
        if selection =='1': 
            key = ''.join(random.choice(text) for i in range(len(msg)))
            print("Randomly generated key: " + key)
            print(encrypt(msg, key))
            break 
        elif selection == '2':
            decKey = input("Decryption Key: ")
            print(decrypt(msg, decKey)) 
            break
        else: 
            print("Error: Invalid Option Selected")
            break



    