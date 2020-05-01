#Atbash Cipher Encoder/Decoder
alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
punctuation = " .?!:;,'\"\\"

print("Welcome to the Atbash Cipher Encoder/Decoder.")
use_default_alphabet = input("Would you like to use the standard English alphabet (ABCDEFGHIJKLMNOPQRSTUVWXYZ)?\nEnter (y/n): ").upper()
while use_default_alphabet != 'Y' and use_default_alphabet != 'N':
    use_default_alphabet = input("Unrecognized option. Please enter either y or n to indicate whether you would like to use the Standard English Alphabet: ").upper()

if use_default_alphabet == 'N':
    alphabet = input("Please enter your custom alphabet (in uppercase letters): ").upper()
    # TODO: check for duplicates(?)

ciphertext = input("Enter the text: ").upper()

for i in range(len(ciphertext)):
    if ciphertext[i] not in alphabet and ciphertext[i] not in punctuation:
        raise Exception("Character " + ciphertext[i] + " at index " + str(i) + " is not in the alphabet.")

rev_alphabet = alphabet[::-1]

modified_text = ""
for i in range(len(ciphertext)):
    if ciphertext[i] in punctuation:
        modified_text += ciphertext[i]
    else:
        ind = alphabet.index(ciphertext[i])
        modified_text += rev_alphabet[ind]
print(modified_text)

leave = input("Press enter to exit.")
