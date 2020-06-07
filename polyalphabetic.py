# Polyalphabetic Shift Encoder/Decoder

alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
punctuation = " .?!:;,'\"\\"

print("Welcome to the Polyalphabetic Shift Encoder/Decoder.")
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

for i in range(len(ciphertext)):
    if ciphertext[i] not in alphabet and ciphertext[i] not in punctuation:
        raise Exception("Character " + ciphertext[i] + " at index " + str(i) + " is not in the alphabet.")

substitution = input("Enter the substitution text: ").upper()
for i in range(len(substitution)):
    if substitution[i] not in alphabet and substitution[i] not in punctuation:
        raise Exception("Character " + substitution[i] + " at index " + str(i) + " is not in the alphabet.")

if encrypt_decrypt == 'E':
    encrypted_text = ""
    if use_default_alphabet == 'Y':
        for i in range(len(ciphertext)):
            if ciphertext[i] in punctuation:
                encrypted_text += ciphertext[i]
            else:
                print((ord(ciphertext[i]) + ord(substitution[i % len(substitution)])) % 26)
                encrypted_text += chr(ord("A") + (ord(ciphertext[i]) + ord(substitution[i % len(substitution)])) % 26)
    else:
        pass
    print(encrypted_text)

else:
    decrypted_text = ""
    if use_default_alphabet == 'Y':
        pass
    else:
        pass

    print(decrypted_text)

leave = input("Press enter to leave.")