## Trabalhando com leituras de arquivos
## Entendendo como funciona json
## BOM DIA!!!!

## Como abrimos um arquivo salvo em texto no python?
minhaInfo1 = open("dadosAula04.txt", "r", encoding='utf8')
print(minhaInfo1.read())

## Uma vez lido, o ponteiro do arquivo não volta ao inicio. Com isso,
## caso tentemos ler novamente, não conseguiremos nenhuma informação.
print(minhaInfo1.read())

## Para evitar problemas e estresse, utilize o comando abaixo quando necessário
minhaInfo1.seek(0,0)
print(minhaInfo1.read())

## Assim como podemos ler arquivos em texto, também podemos escrever neles.
minhaInfo2 = open('dadosAula04.txt', 'w')
minhaInfo2.write('Olá, mundo!')
minhaInfo2.close()

print(minhaInfo2.read()) ## Nossos arquivos são sobreescritos por novos dados