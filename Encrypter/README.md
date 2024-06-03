# Criptografador Fernet para arquivos de texto

Este script python criptografa e descriptografa arquivos de texto .txt ou aqrquivos compostos por texto em formato utf-8.
Através do módulo [Cryptography](https://github.com/pyca/cryptography) este script criptografa aquivos de texto usando Fernet, impossibilitando que o arquivo seja lido ou modificado sem saber sua chave ou token. Fernet usa AES em modo CBC usando uma chave de 128bits com padding PKCS7 e HMAC usando SHA256 para autenticação. Utiliza chave simétrica e este script também utiliza salt usando os.urandom() para a chave.

## fernetEcrypter
Script para ser usado como Módulo para facilitar criptografação utilizando Fernet. Utilizando a classe fernetEncrypter pode ser criptografar ou descriptografar um arquivo. Possibilita a cripgrafção de módo extremamente fácil tornando sua implementação em projetos python muito simples, sendo necessário somente uma função para criptografar um arquivo.

class fernetEncrypter(password, filepath, saltpath)
 - password: Senha, em bytes, utilizada para criar chave, é necessario lembrar desta senha para conseguir descriptografar um arquivo, NUNCA compartilhar esta senha.
 - filepath: Caminho completo do arquivo a ser criptografado e descriptografado
 - saltpath: Caminho onde o arquivo salt.fernet está localizado, se não existir será criado. Se não especificado será utilizado o mesmo local do script fernetEncrypter

encrypt()
 - Criptografa o arquivo associado ao objeto, mudando sua extensão para '.fernet' e guardando a extensão antiga dentro dp arquivo.

decrypt()
 - Descriptografa o arquivo associado ao objeto, mudando sua extensão para a extensão original guardada dentro do arquivo. Caso a chave esteja escreve no console 'InvalidToken Error' e para o processo.

## fileEncrypter
Script que usa fernetEcrypter para demonstrar o processo de criptpgrafação, usando apenas o módulo consegue protejer um arquivo de forma muito fácil e rápida.
