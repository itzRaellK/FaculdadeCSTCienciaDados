## Trabalhando com pacote Matplotlib
## Este pacote é responsável por auxiliar na visualização gráfica de dados
## em outras palavras, vai criar gráficos com os dados que manipularemos no futuro
## Bom dia!!!!

## Primeiro passo, importa o pacote matplotlib
## Aparentemente, na versão mais atual do Python(3.10.4), a importação não funciona corretamente
import matplotlib.pyplot as plt
import numpy as np

'''
x = np.linspace(9.99, 99, 20)
##print(x)
y = x ** 2
##print(y)

plt.plot(x, y)
plt.xlabel('Eixo x')
plt.ylabel('Eixo y')
plt.title('Gráfico para estudo')
'''

##plt.show()

materiasFaculdade = ('LÍNGUA BRASILEIRA DE SINAIS', 'LINGUAGEM DE BANCO DE DADOS', 'INFERÊNCIA ESTATÍSTICA', 'PROGRAMAÇÃO ESTATÍSTICA')
eixoX = np.arange(len(materiasFaculdade)) 
eixoY = [6.0, 8.5, 9.0, 8.0]

plt.bar(eixoX, eixoY, align = 'center')
plt.xticks(eixoX, materiasFaculdade)
plt.ylabel('Notas')
plt.title('Notas das materias na faculdade')

plt.show()

## Como podemos ver, o gráfico está sendo gerado com base nos dados que foram passados
## basta passar os dados que queremos plotar e o gráfico será gerado automaticamente
## O gráfico é gerado na mesma pasta do arquivo que está sendo executado