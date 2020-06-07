#Affine Cipher Encoder/Decoder
alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
punctuation = " .?!:;,'\"\\"

print("Welcome to the Affine Cipher Encoder/Decoder.")
use_default_alphabet = input("Would you like to use the standard English alphabet (ABCDEFGHIJKLMNOPQRSTUVWXYZ)?\nEnter (y/n): ").upper()
while use_default_alphabet != 'Y' and use_default_alphabet != 'N':
    use_default_alphabet = input("Unrecognized option. Please enter either y or n to indicate whether you would like to use the Standard English Alphabet: ").upper()

if use_default_alphabet == 'N':
    alphabet = input("Please enter your custom alphabet (in uppercase letters): ").upper()
    # TODO: check for duplicates(?)

encrypt_decrypt = input("Would you like to encrypt or decrypt your text?\nEnter (e/d): ").upper()
while encrypt_decrypt != 'E' and encrypt_decrypt != 'D':
    encrypt_decrypt = input("Unrecognized option. Please enter either e or d to indicate whether you would like to encrypt or decrypt your text: ").upper()

if encrypt_decrypt == 'E':
    ciphertext = input("Enter your text to be encrypted: ").upper()
else:
    ciphertext = input("Enter your text to be decrypted: ").upper()

