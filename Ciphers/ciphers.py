import string

def main():
    x = int(input("Este é um projeto em Python para criptografar frases usando cifras\n" + "Você gostaria de (1)criptografar ou (2)descriptografar? "))
    while x != 1 or x != 2:
        x = int(input("Por favor digite 1 ou 2: "))
    message = input("Digite a sua mensagem: ")
    cipher = int(input("Qual cifra deseja usar? (1)Cifra de Caesar (2)Caixa de Caesar (3)Código Morse: "))
    while cipher != 1 or cipher != 2 or cipher != 3:
        cipher = int(input("Porfavor digite 1, 2 ou 3: "))
    match cipher:
        case 1:
            n = int(input("Digite o offset: ")) % 26
            n = n if x == 1 else -n
            caesar(message, n)
        case 2:
            w = int(input("Digite a largura da caixa: "))
            caesarBox(message, x, w)
        case 3:
            morse(message, x)

def caesar(message: str, n: int):
    alphabetLower = string.ascii_lowercase
    alphabetUpper = string.ascii_uppercase
    encryptedMessage = []
    for i in range(len(message)):
        if alphabetLower.count(message[i]) != 0:
            alphabetLetter = alphabetLower.index(message[i])
            encryptedMessage.insert(i, alphabetLower[(alphabetLetter+n)%26])
        elif alphabetUpper.count(message[i]) != 0:
            alphabetLetter = alphabetUpper.index(message[i])
            encryptedMessage.insert(i, alphabetUpper[(alphabetLetter+n)%26])
        else: encryptedMessage.insert(i, message[i])
    return print("".join(encryptedMessage))

def caesarBox (message: str, x: int, w: int):
    message = message.replace(" ", "")
    if len(message) % w != 0:
        filler = input("Digite uma letra para preencher a caixa: ")
        while filler == " ":
            filler = input("Digite uma letra para preencher a caixa: ")
        while len(message) % w != 0:
            message = message + filler
    print(message)
    h = int(len(message) / w)
    encryptedMessage = []
    match x:
        case 1:
            caesarBox = [message[i:i+w] for i in range (0, len(message) , w)]
            print(caesarBox)
            for i in range(w):
                    j = 0
                    while j < h:
                        encryptedMessage.append(caesarBox[j][i])
                        j += 1
        case 2:
            caesarBox = [message[i:i+h] for i in range (0, len(message) , h)]
            print(caesarBox)
            for i in range(h):
                    j = 0
                    while j < w:
                        encryptedMessage.append(caesarBox[j][i])
                        j += 1
    return print("".join(encryptedMessage))

def morse(message: str, x: int):
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
    match x:
        case 1:
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
        case 2:
            encryptedMessage = message.split(" ")
            message = []
            for i in range(len(encryptedMessage)):
                if encryptedMessage[i] in morseNum.values():
                    insert = list(morseNum.keys())[list(morseNum.values()).index(encryptedMessage[i])]
                    message.insert(i, insert)
                elif encryptedMessage[i] in morseAlphabet.values():
                    insert = list(morseAlphabet.keys())[list(morseAlphabet.values()).index(encryptedMessage[i])]
                    message.insert(i, insert)
                elif encryptedMessage[i] == "/":
                    message.insert(i, " ")
                else:
                    message.insert(i, encryptedMessage[i])
            return print("".join(message))
try:
    main()
except ValueError:
    print("Erro: Digite um número")