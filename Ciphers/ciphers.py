import string

def main():
    x = int(input("This is a encryption assisting tool made as a Python Project\n" + "Do you wish to (1)encrypt or (2)decrypt? "))
    match x:
        case 1:
            message = input("Please write the message you wish to encrypt: ")
            n = int(input("Write the shift/offset: "))
            print(caesar(message, n))
        case 2:
            message = input("Please write the message you wish to decrypt: ")
            n = int(input("Write the shift/offset: "))
            print(caesarDecode(message, n))

def caesar(message: str, n: int):
    if n > 26:
        n -= 26
    alphabet = string.ascii_lowercase
    cryptAlphabet = ["-" for i in alphabet]
    for i in range(len(cryptAlphabet)):
        new_i = i + n
        if new_i > 25:
            new_i -= 26
        cryptAlphabet[i] = alphabet[new_i]
    encryptedMessage = []
    for i in range(len(message)):
        if alphabet.count(message[i]) != 0:
            alphabetLetter = alphabet.index(message[i])
            cryptLetter = cryptAlphabet[alphabetLetter]
            encryptedMessage.insert(i, cryptLetter)
        else: encryptedMessage.insert(i, message[i])
    return "".join(encryptedMessage)

def caesarDecode(message: str, n: int):
    if n > 26:
        n -= 26
    return(caesar(message, -n))

main()