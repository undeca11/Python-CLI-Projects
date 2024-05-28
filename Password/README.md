Gerador de senhas em Python utilizando o módulo secrets e função de teste da força de senhas usando zxcvbn.

A CISA (Cybersecurity & Infrastructure Security Agency) recomenda que para que uma senha seja segura ela necessita atender alguns requisitos, como:
 - Tamanho: Pelo menos 16 caracteres
 - Aleatoriedade: Uma mistura de letras, número e símbolos, ou 5-7 palavras
 - Único: Deve ser usada em somente uma conta, nunca repetida

Porém poder ser difícil lembrar ou criar diversas senhas diferentes, assim surgem gerenciadores de senhas, que criam e guardam senhas seguras para o usuário.

Este projeto tem como finalidade criar senhas senhas seguras para o usuário e testar a força e segurança de uma senha, dando um parecer sobre as suas fraquezas e forma de melhorar. Este projeto não armazena nem transfere dados, apenas cria as senhas.

Para criar as senhas é usado o módulo secrets ao invés do mais conhecido random, pois o módulo secrets é o mais indicado para questões voltadas à segurança devido ao seu algorítimo de aleatoriedade mais seguro. O usuário pode criar uma senha composta de letras e números, ou letras, números e símbolos ou somente usando palavras do português. Para a criar senha utilizando somente palavras o programa lê o arquivo palavras.txt e escolhe n palavras da lista, assim criando uma senha aleatória, longa e que pode ser lembrada de forma mais fácil. Para adicionar mais palavras a lista é só escrever no arquivo palavras.txt e separar as palavras usando vírgula e um espaço.

Para o teste de senhas foi utilizado o módulo zxcvbn (https://github.com/dropbox/zxcvbn) da Dropbox, que quantifica de forma eficiente e mais complexa do que outros algorítimos, além de prover feedback sobre a senha. O feedback foi traduzido pelo código e repassado ao usuário.
