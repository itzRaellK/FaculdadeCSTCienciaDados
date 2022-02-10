## Programação orientada a objetos e suas complexidades
## Lembre-se, metodos são funções dentro de classes

class Retangulo():
    base = 2
    altura = 2
    def __init__(self, initRetangulo): ## Inicializador, função que constroi o objeto
        self.retangulo = initRetangulo
    
    def setRetangulo(self, newRetangulo): ## Função que define a criação de novos objetos a partir do inicializador
        self.retangulo = newRetangulo

    def getRetangulo(self): ## Função que retorna o valor padrão do objeto
        return self.retangulo
    
    def calcRetangulo(self, base, altura): ## Função responsável por calcular o valor do retangulo
        return base * altura

medida = 'cm2'

retangulo1 = Retangulo(1) ## Instanciando o objeto
print(Retangulo.altura) ## Acessando atributos de classe - valor: 2
print(Retangulo.base)   ## Acessando atributos de classe - valor: 2

print(retangulo1.getRetangulo()) ## Atributo de instância - valor:2

retangulo1.setRetangulo(10) ## Setando um novo valor - valor: 10
print(retangulo1.getRetangulo()) ## Novo atributo de instância - valor: 10

valorFinal = retangulo1.calcRetangulo(2, 10) ## Guardando em uma variável o valor final do calculo do retangulo
print(valorFinal, medida) 

## ----------------------------------------------------------------------------------------------

retangulo2 = Retangulo(1)
valorFinal = retangulo2.calcRetangulo(50, 3)
print(valorFinal, medida)

retangulo3 = Retangulo(1)
valorFinal = retangulo3.calcRetangulo(15, 7)
print(valorFinal, medida)