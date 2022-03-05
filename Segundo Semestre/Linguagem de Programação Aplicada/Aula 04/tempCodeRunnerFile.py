## Continuação da aula04
## Com o comando r+, podemos ler e escrever no mesmo arquivo


minhaInfo3 = open('dadosAula04.txt', 'r+')
minhaInfo3.write('Nome: Israel Kessler Ramos, Idade: 26, Humor: 64%')
minhaInfo3.seek(0,0)
##minhaInfo3.close()


print(minhaInfo3.read())