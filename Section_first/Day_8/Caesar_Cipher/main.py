alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

#TODO-1: Create a function called 'encrypt' that takes the 'text' and 'shift' as inputs.

def encrypt(extext):
    new_word = ""
    for i in extext:
        index = alphabet.index(i)
        index = index + shift
        if index > 25:
            sum = index - 25
            index = alphabet.index("a") + sum-1
            new_word += alphabet[index]
        else:
            new_word += alphabet[index]   
    print(new_word)

encrypt(text)


#Still problem with encrypting

def decrypt(extext):
    new_word = ""
    for i in extext:
        index = alphabet.index(i)
        index = index - shift
        if index < 0:
            sum = 25 - index
            index = alphabet.index("a") + sum-1
            new_word += alphabet[index]
        else:
            new_word += alphabet[index]   
    print(new_word)

