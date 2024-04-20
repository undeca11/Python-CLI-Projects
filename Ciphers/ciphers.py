import string

def main():
    x = int(input("This is a encryption assisting tool made as a Python Project\n" + "Do you wish to (1)encrypt or (2)decrypt? "))
    message = input("Please write your message= ")
    n = int(input("Write the shift/offset= ")) % 26
    match x:
        case 1:
            print(caesar(message, n))
        case 2:
            print(caesar(message, -n))

def caesar(message= str, n= int):
    alphabetLower = string.ascii_lowercase
    alphabetUpper = string.ascii_uppercase
    encryptedMessage = []
    for i in range(len(message)):
        if alphabetLower.count(message[i]) != 0:
            alphabet = alphabetLower
        elif alphabetUpper.count(message[i]) != 0:
            alphabet = alphabetUpper
        else:
            alphabet = False
        if alphabet != False:
            alphabetLetter = alphabet.index(message[i])
            encryptedMessage.insert(i, alphabet[alphabetLetter+n])
        else: encryptedMessage.insert(i, message[i])
    return "".join(encryptedMessage)

main()