#### Um código simples para um jogo de adivinhar qual é o número correto.

numeroCorreto = 37

print("Acerte qual é o número correto!")

numeroDigitado = int(input("Digite um número:"))

if numeroDigitado == numeroCorreto:
    print('Número correto!!!!')
else:
    print('Tente novamente!')