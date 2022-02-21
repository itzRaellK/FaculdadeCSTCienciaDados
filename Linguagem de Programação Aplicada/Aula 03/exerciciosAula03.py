## Exercícios de fixação da aula 03
## Vamo bora!!!!

import numpy as np
import pandas as pd

## O que será printado com o comando vet.shape no código abaixo?
vet = np.array(['A','B','C'])
print(vet.shape) ## O resultado printado é o tamanho do array, ou seja, vet = 3

## Qual o código correto para que se crie um dataframe com as informações de SO e vendas?
dados = {'SO': ['Android','iOS','Windows'], 'Vendas': [80,18,2]}
df = pd.DataFrame(dados)
print(df)

## Qual código cria corretamente uma matriz corretamente?
matriz = np.array([[1,2,3],[4,5,6],[7,8,9]])
print(matriz)