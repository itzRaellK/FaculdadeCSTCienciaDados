

## Neste código eu resolvi melhorar o exercício anterior, onde o número secreto era previamente definido.
## Agora o número é gerado aleatoriamente de acordo com o range (intervalo) definido

import random

numeroSecreto = random.randrange(1, 11)
fraseInicial = 'Que comece o jogo!'
fraseQuestionadora = 'Digite o seu número:'
fraseVencedora = 'Parabéns, você acertou o número secreto!!!'
frasePerdedora = 'Infelizmente você errou! Tente de novo!'

print(fraseInicial) ## JOGO STARTA!

numeroDigitado = int(input(fraseQuestionadora)) ## O jogador digita um número

while numeroDigitado != numeroSecreto:
    print(frasePerdedora)
    numeroDigitado = int(input(fraseQuestionadora)) ## Caso erre, o jogador pode digitar outro número
else:
    print(fraseVencedora) ## Caso acerte o número, o programa finaliza com a mensagem de parabéns