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
    sugestao = zx['feedback']['suggestions']
    
    print(f'Aqui está a análise da sua senha:\nNota {score}/4\nDemoraria {traduzir(tempo,'tempo')} para adivinhar')
    if aviso != '': print(traduzir(aviso, 'aviso'))
    if sugestao != '': print(traduzir(sugestao, 'sugestao'))

def traduzir(frase, tipo):
    traducao = ''
    match tipo:
        case 'tempo':
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
        case 'aviso':
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
        case 'sugestao':
            for i in frase:
                match i:
                    case 'Use a few words, avoid common phrases.':
                        frase[frase.index('Use a few words, avoid common phrases.')] = 'Use algumas palavras, evite frases comuns.'
                    case 'No need for symbols, digits, or uppercase letters.':
                        frase[frase.index('No need for symbols, digits, or uppercase letters.')] = 'Não precisa de símbolos,dígitos ou letras maiúsculas.'
                    case 'Add another word or two. Uncommon words are better.':
                        frase[frase.index('Add another word or two. Uncommon words are better.')] = 'Adicione uma palavra ou duas. Palavras incomuns são melhores.'
                    case 'Use a longer keyboard pattern with more turns.':
                        frase[frase.index('Use a longer keyboard pattern with more turns.')] = 'Use um padrão de teclas com mais "voltas".'
                    case 'Avoid repeated words and characters.':
                        frase[frase.index('Avoid repeated words and characters.')] = 'Evite palavras e caracteres repetidos.'
                    case 'Avoid sequences.':
                        frase[frase.index('Avoid sequences.')] = 'Evite sequências.'
                    case 'Avoid recent years':
                        frase[frase.index('Avoid recent years')] = 'Evite anos recentes.'
                    case 'Avoid years that are associated with you.':
                        frase[frase.index('Avoid years that are associated with you.')] = 'Evite anos que são associados com você.'
                    case 'Avoid dates and years that are associated with you':
                        frase[frase.index('Avoid dates and years that are associated with you')] = 'Evite anos e datas que são associados com você.'
                    case "Capitalization doesn't help very much.":
                        frase[frase.index("Capitalization doesn't help very much.")] = 'Capitalização não ajuda muito.'
                    case 'All-uppercase is almost as easy to guess as all-lowercase':
                        frase[frase.index('All-uppercase is almost as easy to guess as all-lowercase.')] = 'Usar somente letras maiúsculas são tão fáceis de adivinhar quanto letras minúsculas.'
                    case "Reversed words aren't much harder to guess.":
                        frase[frase.index("Reversed words aren't much harder to guess.")] = 'Palavras invertidas não são tão mais difíceis de adivinhar.'
                    case "Predictable substitutions like '@' instead of 'a' don't help very much":
                        frase[frase.index("Predictable substitutions like '@' instead of 'a' don't help very much.")] = 'Substituições comuns como "@" ao invés de "a" não ajudam muito'
            traducao = ' '.join(frase)
    return traducao

main()