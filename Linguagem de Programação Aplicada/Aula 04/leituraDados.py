## Revisando os estudos sobre leitura de dados com python rs
## Boa noite!!!!!!!!!!!!!!!!!


## Primeiro precisamos armazenar os dados que queremos ler em uma variável
teste1 = open('dados2.txt', 'r', encoding='utf8')
print(teste1.read()) ## Agora temos acesso as informações dentro do arquivo e podemos ler

## com o comando abaixo, resetamos o "ponteiro" para o inicio do arquivo
## Ponteiro seria, como se fosse um cursor, onde está o arquivo
## Ao ler o arquivo, o ponteiro se move para o final dele e não retorna automaticamente
teste1.seek(0,0)

## ------------------------------------------------------------------------------------------
## Podemos sobreescrever dados no arquivo em questão com os comandos abaixo
teste2 = open('dados3.txt', 'w')
teste2.write('Testando e aplicando estudos de escrita e leitura de dados em arquivos de texto!')
teste2.close()

teste2 = open('dados3.txt', 'r', encoding='utf8')
print(teste2.read(),'\n')
teste2.close()

## ------------------------------------------------------------------------------------------
## Podemos também, escrever dados no arquivo em questão com os comandos abaixo
teste3 = open('dados4.txt', 'r+') ## O arquivo está vazio, então escreveremos dados novos nele
teste3.write('Olá, boa noite! Hoje o dia foi bem puxado. Comecei o dia com uma boa notícia e um teste logo a cinco da manhã.' 
                + ' Terminei o dia com outra boa notícia e um belo teste novamente.')
teste3.close()

teste3 = open('dados4.txt', 'r')
print(teste3.read())