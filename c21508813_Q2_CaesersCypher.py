# ---------------------------------------------
# Advanced Security Assignment 1, Q2 and q3
# Author: Haroun Kassouri
# Date: 04/10/2024
# Details; Program to implement Caeser Cipher
# ---------------------------------------------

class Solution(object):
    def encryptCaesarCipher(self, cipher_text, shift):
        text = ''  
        
        for char in cipher_text:
            if char.islower():  
                text += chr((ord(char) - ord('a') + shift) % 26 + ord('a'))
            elif char.isupper():
                text += chr((ord(char) - ord('A') + shift) % 26 + ord('A'))
            else:
                text += char
        
        return text


while True:
    encrpyt_decrpyt = input('Would you like to encrypt or decrypt: (0 to exit)\n')

    cipher_text = "Hello, I am Haroun Kassouri"
    shift = 3 
        
    sol = Solution()
    encrypted_message = sol.encryptCaesarCipher(cipher_text, shift)
    
    if encrpyt_decrpyt == 'Encrypt' or encrpyt_decrpyt == 'encrypt':
        encrypted_message = sol.encryptCaesarCipher(cipher_text, shift)
        print('\n------------------------------------------')
        print('Encrypted Message:', encrypted_message)
        print('------------------------------------------')
        break
    elif encrpyt_decrpyt == 'Decrypt' or encrpyt_decrpyt == 'decrypt':
        decrypted_message = sol.encryptCaesarCipher(cipher_text, -shift)
        print('\n------------------------------------------')
        print('Decrypted Message:', decrypted_message)
        print('------------------------------------------')
        break
    elif encrpyt_decrpyt == '0':
        print("Exiting program.")
        break
    else:
        print('\n------------------------------------------')
        print('Please Enter Encrypt or Decrypt')
        print('------------------------------------------')