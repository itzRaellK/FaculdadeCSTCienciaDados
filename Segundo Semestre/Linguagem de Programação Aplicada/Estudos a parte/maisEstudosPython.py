
nome = "Israel"
print("Vamos brincar de adivinhe meu nome?")

nomeDigitado = input()
if nomeDigitado == nome:
    print("Você acertou!!!")
else:
    print("Você errou! Tente novamente!") 
    
# -----------------------------------------------

print("Vou te zuar, preste atenção!")

dado1 = input("Digite um numero:")
dado2 = input("Digite um nome:")
dado3 = input("Digite sua idade:")

print("AMAURI bronze lixo!")

# -------------------------------------------------------

def multNumeros (a,b):
    resultado = a * b
    return resultado
    
a = int(input("Digite um número:"))
b = int(input("Digite um número:"))

print("Resultado da multiplicação",multNumeros(a,b))

# ------------------------------------------------------------
import math

def calculoBizarro (xBarra, x, n):
    resultado = xBarra - x / ((math.sqrt(n)) * (math.sqrt(n)))
    return print(round(resultado, 4))
''' Utilizando o round('valor', 4) consigo limitar a quantidade
   de casas decimais que irão aparecer no resultado printado! '''
   
xBarra = float(input("Digite o valor de xBarra:"))
x = float(input("Digite o valor de x:"))
n = float(input("Digite o valor de n:"))

calculoBizarro(xBarra, x, n)