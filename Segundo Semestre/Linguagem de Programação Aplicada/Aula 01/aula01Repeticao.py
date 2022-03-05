
### Abaixo veremos exemplos de códigos com repetições (For e While)

from re import I

'''numeroQualquer = 0

while numeroQualquer <= 10:
    print(numeroQualquer)
    numeroQualquer += 2'''

#### ----------------------------------------------------------

'''numeroDigitado = int(input('Acerte o número secreto:'))

while numeroDigitado != 37:
    numeroDigitado = int(input('Tente novamente:'))
if numeroDigitado == 37:
    print('Você acertou!')'''

#### ----------------------------------------------------------

nomes = ['Israel Kessler', 'Amauri Lucas', 'Douglas Dias']
print(nomes[2])
print(nomes[:3])

### Adicionando elementos no array nomes
nomes.append('Matheus Dak')
copia = nomes[:4]
print(copia)

### Deletando elementos do array nomes... Tchau DOUGLAS DIAS!!!! HAHAHAHA
del nomes[2]
print(nomes)

#### ----------------------------------------------------------

### Discionario em Python 
produto_quantidade={'Tecplus 18kg': 10, 'Tecplus 4kg': 32, 'Cimento CPIII': 79, 'Coral Pinta Piso Amarelo Demarcação': 7}
print(produto_quantidade)

produto01 = print('Tecplus 18kg', produto_quantidade['Tecplus 18kg'])