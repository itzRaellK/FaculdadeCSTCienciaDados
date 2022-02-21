## Exercícios da aula 02

class Animal:
    def __init__(self, raca, idade, cor):
        self.raca = raca
        self.idade = idade
        self.cor = cor

a1 = Animal('felino', 15 , 'marrom')

print(a1.cor == 'marrom')


class Frutas():
    def add(self, f):
        return f

objFrutas = Frutas()
vetfrutas = []

fruta = objFrutas.add('Uva')

vetfrutas = vetfrutas.append(fruta)
print(fruta)
