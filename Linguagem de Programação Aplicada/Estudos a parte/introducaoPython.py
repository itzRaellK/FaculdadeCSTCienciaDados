# Primeira Aula com Python - Linguagem de Programação Aplicada
# Vamo que vamo! Boa noite!

# OPERADORES ARITIMÉTICOS
from operator import truediv


print(1 + 1, 2 - 2, 3 * 5, 4 / 1, 10 % 2)
num1 = 10
num2 = 5
print(num1 > num2) # true
print(num1 < num2) # false

# OPERADORES DE ATRIBUIÇÃO
num1 = 5
num2 = 55
print(num1 > num2) # false
print(num1 != num2) # true

# OPERADORES DE COMPARAÇÃO
numSecreto = 0
print(numSecreto) # valor 0
numSecreto += 100 
print(numSecreto) # valor 100
numSecreto -= 50
print(numSecreto) # valor 50
numSecreto += 1
print(numSecreto) # valor 51

# OPERADORES LÓGICOS
verdade = True
falso = False

print(verdade and falso) # false
print(verdade or falso) # true
print(not verdade) # false
print(not falso) # true


## --------------------------------------------------------------------------------------------

# listas
frutas = ['goiaba', 'uva', 'maca']
print(frutas)

# dicionarios
nome_sobrenome = {'Israel':'Kessler', 'Amauri':'Lucas'}
print(nome_sobrenome)

# tupla
animais = ('leao', 'tigre', 'sapo')
print(animais)

