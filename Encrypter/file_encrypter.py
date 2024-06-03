import fernet_encrypter as fe

path = input('Digite o caminho do arquivo: ').replace('\\','/')
pas = input('Qual a senha: ').encode()
mode = input('Deseja (1) criptografar ou (2) Descriptografar: ')

cript = fe.FernetEncrypter(pas, path)

while True:
    try:
        mode = input('Deseja (1) criptografar, (2) Descriptografar ou (3) Sair do programa: ')
        match int(mode):
            case 1:
                print("Opção 1")
            case 2:
                print("Opção 2")
            case 3:
                print('\nPrograma encerrado!')
                quit()
            case _:
                raise ValueError
    except ValueError:
        print('Por favor, digite algo válido!')
