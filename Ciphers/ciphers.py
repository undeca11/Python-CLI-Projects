import string

def main():
    x = int(input("This is a encryption assisting tool made as a Python Project\n" + "Do you wish to (1)encrypt or (2)decrypt? "))
    message = input("Please write your message: ")
    cipher = int(input("What cipher do you wish to use? (1)Caesar Cipher (2)Caesar Box (3)Morse Code "))
    match x:
        case 1:
            match cipher:
                case 1:
                    n = int(input("Write the shift/offset= ")) % 26
                    caesar(message, n)
                case 3:
                    morse(message)
        case 2:
            match cipher:
                case 1:
                    n = int(input("Write the shift/offset= ")) % 26
                    caesar(message, -n)
                case 3:
                    morse(message)

def caesar(message= str, n= int):
    alphabetLower = string.ascii_lowercase
    alphabetUpper = string.ascii_uppercase
    encryptedMessage = []
    for i in range(len(message)):
        if alphabetLower.count(message[i]) != 0:
            alphabetLetter = alphabetLower.index(message[i])
            encryptedMessage.insert(i, alphabetLower[alphabetLetter+n])
        elif alphabetUpper.count(message[i]) != 0:
            alphabetLetter = alphabetUpper.index(message[i])
            encryptedMessage.insert(i, alphabetUpper[alphabetLetter+n])
        else: encryptedMessage.insert(i, message[i])
    return print("".join(encryptedMessage))

def morse(message= str):
    message = message.lower()
    morseNum = {
    "0" : "-----",
    "1" : ".----",
    "2" : "..---",
    "3" : "...--",
    "4" : "....-",
    "5" : ".....",
    "6" : "-....",
    "7" : "--...",
    "8" : "---..",
    "9" : "----."
}
    morseAlphabet = {
    "a": ".-",
    "b": "-...",
    "c": "-.-.",
    "d": "-..",
    "e": ".",
    "f": "..-.",
    "g": "--.",
    "h": "....",
    "i": "..",
    "j": ".---",
    "k": "-.-",
    "l": ".-..",
    "m": "--",
    "n": "-.",
    "o": "---",
    "p": ".--.",
    "q": "--.-",
    "r": ".-.",
    "s": "...",
    "t": "-",
    "u": "..-",
    "v": "...-",
    "w": ".--",
    "x": "-..-",
    "y": "-.--",
    "z": "--.."
}
    encryptedMessage = []
    for i in range(len(message)):
        if message[i] in morseNum:
            insert = morseNum[message[i]]
            encryptedMessage.insert(i, insert)
        elif message[i] in morseAlphabet:
            insert = morseAlphabet[message[i]]
            encryptedMessage.insert(i, insert)
        elif message[i] == " ":
            encryptedMessage.insert(i, "/")
        else: 
            encryptedMessage.insert(i, message[i])
    return print(" ".join(encryptedMessage))

main()