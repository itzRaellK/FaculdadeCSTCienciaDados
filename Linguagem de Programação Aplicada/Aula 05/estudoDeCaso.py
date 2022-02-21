## BOM DIA!!!
## Trabalhando com estudos de caso em python

'''Como não foi fornecido os dois arquivos necessários para esta aula, vou somente copiar
os códigos e deixa-los guardados para caso eu precise revisitar alguma parte que não compreendi completamente'''

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

paises = ['Estados Unidos', 'Argentina', 'Brasil', 'Alemanha', 'Paraguai']
ouro = np.array([12,26,18,6,7])
prata = np.array([25,19,35,20,9])
bronze = np.array([20,19,15,6,18])

indice = np.arange(len(paises)) ## criamos um indice com o tamanho do array paises

plt.bar(indice, ouro, label='Ouro', color='gold', bottom=prata+bronze)
plt.bar(indice, prata, label='Prata', color='silver', bottom=bronze)
plt.bar(indice, bronze, label='Bronze', color='#CD853F')

plt.xticks(indice, paises)
plt.ylabel('Medalhas')
plt.xlabel('Países')
plt.title('Olimpíadas de 2016')

plt.show()