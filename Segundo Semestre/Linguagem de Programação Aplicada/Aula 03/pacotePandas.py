## Trabalhando com o pacote Pandas do python
## Responsável por manipular planilhas e tabelas de dados

## Trabalha com Series e DataFrames <<--
## Series: conjunto de dados unidimensionais
## DataFrame: conjunto de dados bidimensionais

## Primeiro passo é importar o pacote Pandas
## Aparentemente, na versão mais atual do Python(3.10.4), a importação não funciona corretamente
import pandas as pd

exemplo1 = pd.Series([1, 7, 35, 9, 93, 55, 59])
print(exemplo1)

print(exemplo1.values) ## Podemos obter os valores da Series
print(exemplo1.index) ## Podemos obter os índices da Series

exemplo2 = pd.Series([1, 7, 35, 9, 93, 55, 59], index = ['A', 'B', 'C', 'D', 'E', 'F', 'G'])
print(exemplo2)

print(exemplo2[:3]) ## Esse comando é conhecido como fatiamento ou slicing, obtemos números específicos com ele
print(exemplo2[exemplo2 > 25]) ## Podemos obter os valores que satisfazem uma condição específica

exemplo2['B'] = 99 ## Podemos modificar os valores de uma Series
print(exemplo2)

## ---------------------------------------------------------------------------

dados = {'vendedor': ['vendedor1', 'vendedor2', 'vendedor3', 'vendedor4', 'vendedor5'],
'vendas': [19800, 13000, 13459, 10153, 9865],
'mes': ['julho', 'agosto', 'setembro', 'outubro', 'novembro']}

print(dados)

df = pd.DataFrame(dados) ## Podemos criar um DataFrame com um dicionário
print(df)

print(df[:3]) ## Podemos obter os dados de um DataFrame