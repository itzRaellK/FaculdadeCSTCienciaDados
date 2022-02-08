#---------------------------------------------------------------------------------------------

# TRABALHANDO COM INPUTS E CASTS
altura = float(input('Digite sua altura: '))
peso = float(input('Digite seu peso: '))

# calculando o IMC
imc = peso / (altura * altura)

print('Seu IMC é : ', imc)