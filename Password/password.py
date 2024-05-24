import string
import secrets

def main():
    pass

def criarSenha(x: int, l: int):
    wordChoice = ''
    match x:
        case 1:
            wordChoice = string.ascii_letters + string.digits
        case 2:
            wordChoice = string.ascii_letters + string.digits + string.punctuation
        case 3:
            wordChoice = lerPalavras()
    senha = ''.join(secrets.choice(wordChoice) for i in range(l))
    print(senha)

def lerPalavras():
    palavras = open('palavras.txt', 'r')
    listaPalavras = palavras.split(', ')
    return listaPalavras
    

def testeSenha():
    pass

criarSenha(1, 16)
criarSenha(2, 16)
criarSenha(3, 3)