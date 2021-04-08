MAX_KEY_SIZE = 26
def getMode():
    while True:
        print('Do you wish to encrypt or decrypt a message?')
        mode = input().lower()
        if mode in 'encrypt e decrypt d'.split():
            return mode
        else:
            print('Enter either "encrypt" or "e" or "decrypt" or "d".')


def getMessage():
    print('Enter your message:')
    return input()


def getKey():
    key = 0
    while True:
        print('Enter the key number (1-%s)' % (MAX_KEY_SIZE))
        key = int(input())
        if (key >= 1 and key <= MAX_KEY_SIZE):
            return key



def decryption(message,k):
    key=-k
    plain_text = ''
    for char in message:
        if char.isalpha():
            num = ord(char)
            num += key
            if char.isupper():
                if num > ord('Z'):
                    num -= 26
                elif num < ord('A'):
                    num += 26
            elif char.islower():
                if num > ord('z'):
                    num -= 26
                elif num < ord('a'):
                    num += 26
            plain_text += chr(num)
        else:
            plain_text += char
    return plain_text


def encryption(message,key):
    cipher_text = ''
    for char in message:
        if char.isalpha():
            num = ord(char)
            num += key
            if char.isupper():
                if num > ord('Z'):
                    num -= 26
                elif num < ord('A'):
                    num += 26
            elif char.islower():
                if num > ord('z'):
                    num -= 26
                elif num < ord('a'):
                    num += 26
            cipher_text += chr(num)
        else:
            cipher_text += char
    return cipher_text



mode = getMode()
if mode in 'encrypt e'.split():
    en_message = getMessage()
    en_key = getKey()
    print('Your Encrypted message is:')
    print(encryption(en_message, en_key))
elif mode in 'decrypt d'.split():
    de_message = getMessage()
    de_key = getKey()
    print('Your Decrypted message is:')
    print(decryption(de_message, de_key))




# Sample OutPut

# 1- Encryption
# Do you wish to encrypt or decrypt a message?
# e
# Enter your message:
# This is my project test no: 1 
# Enter the key number (1-26)
# 5
# Your Encrypted message is:   
# Ymnx nx rd uwtojhy yjxy st: 1

# 2- Decryption and wrong command
# Do you wish to encrypt or decrypt a message?
# vrgbr
# Enter either "encrypt" or "e" or "decrypt" or "d".
# Do you wish to encrypt or decrypt a message?      
# d
# Enter your message:
# Ymnx nx rd uwtojhy yjxy st: 1
# Enter the key number (1-26)
# 5
# Your Decrypted message is:
# This is my project test no: 1