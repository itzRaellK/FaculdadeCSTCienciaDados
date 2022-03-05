
### Abaixo mais alguns exemplos, desta vez relacionados aos códigos de condicionais

nota01 = float(input('Digite a primeira nota do aluno:'))
nota02 = float(input('Digite a segunda nota do aluno:'))

resultadoFinal = round((nota01 + nota02) / 2, 1)

if resultadoFinal >= 6:
    print('Aluno aprovado! Nota:', resultadoFinal)
else:
    print('Aluno reprovado! Nota:', resultadoFinal)