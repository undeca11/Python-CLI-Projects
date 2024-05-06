Programa que usa três cifras populares para criptografar e descriptografar mensagens.

A segurança digital é uma área muito importante no mundo moderno, porém a necessidade de codificar mensagem é muito antiga e foram criados diversos métodos para se criptografar mensagens que precisariam se mantidas em segredo e lidas somente por algúem que possuí-se a chave.

Aqui são utilizadas três cifras, a Cifra de Caesar, a Caixa de Caesar e o Código Morse.

- Cifra de Caesar
A Cifra de Caesar é uma cifra de substituição, onde cada letra da mensagem é substituida por outra, porém mantendo o seu exato lugar na frase.

A Cifra de Caesar foi nomeada em homenagem a Júlio César que, segundo Suetónio, a usava com uma troca de três posições para proteger mensagens de significado militar. Ainda que o uso deste esquema por César tenha sido o primeiro a ser registrado, é sabido que outras cifras de substituições foram utilizadas anteriormente.

Se utilizando de uma chave, cada letra "pula" sua posição no alfabeto, por exemplo, com uma chave = 3 a letra A se tornaria a letra D, a letra B se toranria a letra E, e assim por diante. A Cifra de Caesar apenas troca as letras do alfabeto por outras, mantendo suas posições e quantidade de caracteres. A Cifra de Caesar é facilmente identificada pela recorrência de letras, agrupamneto de letras que parecem formar palavras, e comunmente em quebra cabeça existe referncias a palavras como césar, julius, roma, augustus, ave, imperador e etc. Para decodificar a Cifra de Caesar podemos utilizar o mesmo método para a codificação, apenas usando o contrário da chave, se foi usada uma chave de 3 para a codifição, para decodificar usamos uma chave de -3. A Cifra somente codifica letras, por se basear no alfabeto, então caracteres especiais, emojis ou números não vão ser codificados, o que pode ser usado para reconhecer uma Cifra de Caesar. Existem outras formas de codificação como a ROT-47 que inclui caracteres especias indo de ASCII 33 até 126, porém ainda sofre das mesmas fraquezas da Cifra de Caesar original.

Sem saber a chave utilizada é necesário checar utilizando todas as chaves possíveis, o que para um humano pode demorar, mas é algo trivial para uma máquina, assim não sendo recomendado se utilizar fora de contexto de entreterimento.

- Caixa de Caesar
A Caixa de Caesar é um cifra de transposição, onde cada caracter da mensagem muda sua ordem, mas sem substituição do caracter original.

A Caixa de Caesar foi usada no Império Romano, onde uma mensagem era escrita em linhas e colunas em um quadrado, ou retângulo.

Primeiro se define a largura da caixa, que será o número de colunas, e então se escreve em linhas a mensagem.

Por exemplo a palvra Caesar escrita em uma caixa de largura 3 será:
 ___ ___ ___
| C | A | E | 
 ___ ___ ___
| S | A | R |
 ___ ___ ___

Então se reescreve a mensagem a partir das colunas, ficando "CSAAER". Para decifrar a mensagem se faz o processo contrário, usamo a largura da caixa e se escreve a mensagem a usando o numero de linhas. O número de linhas é definido dividindo o número de caracteres pela largura da caixa.

Decoficando CSAAER:
 ___ ___ ___
| C | A | E | 
 ___ ___ ___
| S | A | R |
 ___ ___ ___

Teremos a mesma caixa, e podemos reescrever a mensagem a partir das linhas, tendo CAESAR.

A Caixa de Caesar não dependo de um alfabeto, e reorganiza os caractéres, removendo os espaços. Se usarmos um número de caracteres que não formem um retângulo é necessário adicionar caracteres extras. Como uma cifra de transposição a Caixa de Caesar pode ser reconhecida por ter letras que formam palavras mas em ordem errada, e se o número de caracteres for o de um quadrado perfeito pode ser uma pista mais forte.

- Código Morse
O Código Morse é um alfabeto de letras, caracteres e pontuação, foi inventado em Samuel Morse em 1837 para ser transmitido por pulsos sonoros ou ondas eletromagnéticas. Este sistema representa letras, números e sinais de pontuação apenas com uma sequência de pontos, traços, e espaços. O código Morse é transmitido usando apenas dois estados, ligado e desligado, e é composto por seis elementos:

- Sinal curto, ponto ou 'dit' (·)
- Sinal longo, traço ou 'dah' (-)
- Intervalo entre caracteres (entre pontos e traços)
- Intervalo curto (entre letras)
- Intervalo médio (entre palavras)
- Intervalo longo (entre frases)

O que se é chamado hoje de código Morse difere em parte do que foi originalmente desenvolvido por Morse e seu assistente, uma distinção das sequências do código, incluindo mudanças a onze das letras, foi feita na Alemanha e eventualmente adotada como o padrão mundial como Morse Internacional.

O Código Morse pode ser facilmente identificado pelo seu alfabeto característico, e é facilmente decifrado usando uma tabela ou dicionário.

- O Projeto
O intuito do projeto é aprender sobre formas de codificação antigas e implementar elas em Python usando os conhecimentos adquiridos do meu estudo. Estas cifras não tem potencial de segurança e hoje em dia são somentes utilizadas em contextos de entreterimento.

Foram utiliados conhecimentos de sintaxe, variaveis, funções, listas, dicionários, e exceções. Também foi utilizado o módulo string do Python para obter mais facilmente uma lista das letras do alfabeto.  
