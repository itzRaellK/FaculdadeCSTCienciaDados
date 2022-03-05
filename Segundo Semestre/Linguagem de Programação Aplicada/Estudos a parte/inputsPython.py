#---------------------------------------------------------------------------------------------

# TRABALHANDO COM INPUTS E CASTS
altura = float(input('Digite sua altura: '))
peso = float(input('Digite seu peso: '))

# calculando o IMC
calculo = altura **2
imc = peso / calculo

print('Seu IMC é : ', imc)