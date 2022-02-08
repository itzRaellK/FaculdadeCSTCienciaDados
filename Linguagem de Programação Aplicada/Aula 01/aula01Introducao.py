
### ESTUDOS REFERENTES A AULA 01

### Declarando variáveis em Python
a = 10
b = 20
c = 30
soma = a + b + c
print(soma)

meuNome = 'Israel Kessler Ramos'
print(meuNome)

meuCpf = '125.018.036-80'
print(meuCpf)

### Inputs em Python
nome = input('Digite seu nome completo, por favor:')
print(nome)

peso = float(input('Digite seu peso:'))
altura = float(input('Digite sua altura:'))
imc = round(peso / (altura * altura), 2) # round arrendoda valores e o "2" é a quantidade de casas decimais

print('Seu IMC é:', imc)

### Funções em Python 
nomeDoAmigo = input('Digite o nome do seu melhor amigo:')

def imprimeNome(nomeDoAmigo):
    frase = 'O seu melhor amigo se chama'
    return print(frase, nomeDoAmigo)

imprimeNome(nomeDoAmigo)

import math

def calculo(xBarra, x, n):
    resultado = xBarra - x / ((math.sqrt(n)) * (math.sqrt(n)))
    resultadoArredondado = round(resultado, 4)
    return print('O resultado dessa equação maluca é:', resultadoArredondado)

xBarra = float(input('Digite o valor de xBarra:'))
x = float(input('Digite o valor de x:'))
n = int(input('Digite o valor de n:'))

calculo(xBarra, x, n)
