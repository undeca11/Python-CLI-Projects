import fernetEncrypter as fe

path = input('Digite o caminho do arquivo: ').replace('\\','/')
pas = input('Qual a senha: ').encode()
mode = input('Deseja (1) criptografar ou (2) Descriptografar: ')

cript = fe.fernetEncrypter(pas, path)

while True:
    match int(mode):
        case 1:
            cript.encrypt()
            quit()
        case 2:
            cript.decrypt()
            quit()
        case _:
            mode = input('Deseja (1) criptografar ou (2) Descriptografar: ')