import string
from secrets import choice
from pyperclip import copy
from zxcvbn import zxcvbn

def main():
    print('Este é um projeto em Python para criar senhas e testar sua força.\nVocê gostaria de (1) Criar uma senha ou (2) Testar a força de uma senha?')
    while True:
        x = input()
        if int(x) == 1:
            print('Sua senha sera composta de\n(1) Apenas números e letras\n(2) Números, letras e pontuação\n(3) Palavras em português')
            while True:
                x  = input()
                if int(x) == 1 or int(x) == 2:
                    l = int(input('Escreva o comprimento da sua senha: '))
                    copy(criarSenha(x,l))
                    print('Sua senha foi copiada para a área de trasnferência')
                    quit()
                elif int(x) == 3:
                    l = int(input('Escreva quantas palavras gostaria para sua senha: '))
                    copy(criarSenha(x,l))
                    print('Sua senha foi copiada para a área de trasnferência')
                    quit()
                else:
                    print('Por favor digite 1, 2 ou 3')
        elif int(x) == 2:
            testeSenha()
            quit()
        else:
            print('Por favor digite 1 ou 2')


def criarSenha(x: int, l: int):
    wordChoice = ''
    match int(x):
        case 1:
            wordChoice = string.ascii_letters + string.digits
        case 2:
            wordChoice = string.ascii_letters + string.digits + string.punctuation
        case 3:
            wordChoice = lerPalavras()
    senha = ''.join(choice(wordChoice) for i in range(l))
    return senha

def lerPalavras():
    palavras = open('palavras.txt', 'r')
    listaPalavras = palavras.read().split(', ')
    return listaPalavras
    

def testeSenha():
    x = input('Escreva sua senha para ser testada: ')
    zx = zxcvbn(x, user_inputs=['senha','mudar'])
    score = zx['score']
    tempo = zx['crack_times_display']['online_no_throttling_10_per_second']
    aviso = zx['feedback']['warning']
    
    print(f'Aqui está a análise da sua senha:\nNota {score}/4\nDemoraria {traduzir(tempo,'tempo')} para adivinhar')
    if aviso != '': print(traduzir(aviso, 'aviso'))

def traduzir(frase, tipo):
    traducao = ''
    x = 0
    match tipo:
        case 'tempo':
            x = 1
        case 'aviso':
            x = 2
    match x:
        case 1:
            if frase == 'centuries':
                return 'séculos'
            elif frase == 'less than a second':
                return 'menos de um segundo'
            else:
                match frase[frase.index(" ")+1:-1]:
                    case 'second':
                        traducao = 'segundo'
                        if frase[-1] == 's': traducao += 's'
                    case 'minute':
                        traducao = 'minuto'
                        if frase[-1] == 's': traducao += 's'
                    case 'hour':
                        traducao = 'hora'
                        if frase[-1] == 's': traducao += 's'
                    case 'day':
                        traducao = 'dia'
                        if frase[-1] == 's': traducao += 's'
                    case 'month':
                        traducao = 'mês'
                        if frase[-1] == 's': traducao = 'meses'
                    case 'year':
                        traducao = 'ano'
                        if frase[-1] == 's': traducao += 's'
        case 2:
            match frase:
                case 'Straight rows of keys are easy to guess.':
                    traducao = 'Linhas de teclas consecutivas são fáceis de adivinhar'
                case 'Short keyboard patterns are easy to guess.':
                    traducao = 'Padrões curtos de teclas são fáceis de adivinhar'
                case 'Repeats like "aaa" are easy to guess.':
                    traducao = 'Repetições como "aaa" são fáceis de adivinhar'
                case 'Repeats like "abcabcabc" are only slightly harder to guess than "abc".':
                    traducao = 'Repetições como "abcabcabc" são pouco mais difíceis de adivinhar do que "abc"'
                case 'Sequences like "abc" or "6543" are easy to guess.':
                    traducao = 'Sequências como "abc" ou "6543" são fáceis de adivinhar'
                case 'Recent years are easy to guess.':
                    traducao = 'Anos recentes são muito fáceis de adivinhar'
                case 'Dates are often easy to guess.':
                    traducao = 'Datas são fáceis de adivinhar'
                case 'This is a top-10 common password.':
                    traducao = 'Essa é uma das 10 senhas mais comuns'
                case 'This is a top-100 common password.':
                    traducao = 'Essa é uma das 100 senhas mais comuns'
                case 'This is a very common password.':
                    traducao = 'Essa é uma senha muito comum'
                case 'This is similar to a commonly used password.':
                    traducao = 'Essa senha é muito parecida com uma senha muito comum'
                case 'Names and surnames by themselves are easy to guess.':
                    traducao = 'Usar apenas nomes e sobrenomes deixa a senha muito fácil de se adivinhar'
                case 'Common names and surnames are easy to guess.':
                    traducao = 'Nomes e sobrenomes comuns são muito fáceis de se adivinhar'
                case _:
                    traducao = frase
    return traducao

main()