## Trabalhando com arquivos CSV

## Teremos que usar o Pandas para essa aula
import pandas as pd

## Guardaremos em uma variável o arquivo csv em questão
dados = 'vgsAula04.csv'

## Agora criaremos um Dataframe com os dados do arquivo csv
df = pd.read_csv(dados)
##print(df)

## Podemos trazer dados do inicio e também do fim do arquivo com head() e tail()
print(df.head(5))
print(df.tail(3))

## Podemos manipular apenas colunas selecionadas se quisermos
print(df['Global_Sales'].head(9))
##print(df['Global_Sales'].tail(20))

