## Trabalhando com pacote Numpy
## Este pacote nos traz funções matemáticas e estatísticas
## Permite trabalhar com matrizes e vetores melhor do que no Python puro!
## BOM DIA!!!!

# Primeiro passo é importar o pacote, pois ele não vem como padrão
## Aparentemente, na versão mais atual do Python(3.10.4), a importação não funciona corretamente
import numpy as np

print('\n')

vet = np.array([5.5,6.5,7.8,3.2,6.2,1.8,9.3,8.7]) ## Podemos criar arrays com dados no numpy
print(vet)

vet[7] = 8.5 ## Temos acesso aos elementos e podemos modifica-los
print(vet)

print(vet.shape) ## Podemos obter o tamanho do array com que estamos trabalhando

## ---------------------------------------------------------------------------

vet2 = np.arange(0, 10, 0.75) ## Com a função arange, obtemos uma projeção de um intervalo
print(vet2)
print(vet2.shape)

## ---------------------------------------------------------------------------

vet3 = np.linspace(0, 10) ## Obtemos valores espaçados de forma uniforme
print(vet3)

vet4 = np.linspace(0,10, 5) ## Podemos definir o número de valores que queremos
print(vet4)

## ---------------------------------------------------------------------------

print('\n')
matriz = np.array([[50, 60, 35], [25, 43, 79], [13, 99, 87]]) ## Podemos criar matrizes com dados no numpy
print(matriz)
print(matriz.shape)

## ---------------------------------------------------------------------------

matriz2 = np.random.randn(4,4) ## Podemos criar matrizes com dados aleatórios
print(matriz2)

## Com a biblioteca NumPy, temos acesso a inumeras funções matemáticas e estatísticas
## Podemos usar a função mean para obter a média de um vetor
## Podemos usar a função std para obter a desvio padrão de um vetor
## Podemos usar a função var para obter a variância de um vetor
## Podemos usar a função corrcoef para obter a correlação entre dois vetores
## Podemos usar a função cov para obter a covariância entre dois vetores
## Por aí vai...