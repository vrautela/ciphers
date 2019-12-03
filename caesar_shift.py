#Caesar Shift Encoder
print("Welcome to the Caesar Shift Encoder.")
alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
print(len(alphabet))
punctuation = " .?!:;,'\"\\"
use_default_alphabet = input("Would you like to use the standard English alphabet (ABCDEFGHIJKLMNOPQRSTUVWXYZ)?\nEnter (y/n): ").upper()
while use_default_alphabet != 'Y' and use_default_alphabet != 'N':
    use_default_alphabet = input("Unrecognized option. Please enter either y or n to indicate whether you would like to use the Standard English Alphabet: ").upper() 

if use_default_alphabet == 'N':
    alphabet = input("Please enter your custom alphabet (in uppercase letters): ").upper()
    # should I check for duplicates?

ciphertext = input("Enter your text to be encrypted: ").upper()
for i in range(len(ciphertext)):
    if ciphertext[i] not in alphabet and ciphertext[i] not in punctuation:
        raise Exception("Character " + ciphertext[i] + " at index " + str(i) + " is not in the alphabet.")
print(ciphertext)

num_shift = input("Enter the amount to shift by: ")
while True:
    try:
        num_shift = int(num_shift)
        break
    except ValueError as e:
        num_shift = input("Please enter a whole number amount to shift by: ")

num_shift %= len(alphabet)
encoded_text = ""

if use_default_alphabet == 'N':    
    for i in range(len(ciphertext)):
        if ciphertext[i] in punctuation:
            encoded_text += ciphertext[i]
        else:
            old_char = ord(ciphertext[i]) - ord('A')
            new_char = chr(ord('A') + ((old_char + num_shift) % len(alphabet)))
            encoded_text += new_char
    print(encoded_text)

else:
    letterPos = dict()
    for i in range(len(ciphertext)):
        if ciphertext[i] in punctuation:
            encoded_text += ciphertext[i]
        else:
            if ciphertext[i] not in letterPos:
                targetPos = alphabet.find(ciphertext[i])
                letterPos[ciphertext[i]] = targetPos

            old_char = letterPos[ciphertext[i]]
            new_char = alphabet[(old_char + num_shift) % len(alphabet)]
            encoded_text += new_char
    print(encoded_text)
