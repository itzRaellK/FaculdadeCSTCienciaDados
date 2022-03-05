## Programação orientada a objetos e suas complexidades
## Lembre-se, metodos são funções dentro de classes

class IA():
    def __init__(self, nome, idade, genero):
        self.nome = nome
        self.idade = idade
        self.genero = genero
    
    def saudacao(self):
        return IA.print('Olá Israel Kessler, tudo bem?')
        

alexis = IA('Alexis', 19, 'Feminino',)
print('Nome:',alexis.nome, 'Idade:',alexis.idade, 'Genero:',alexis.genero)

## Não consegui descobrir uma forma de acessar a função saudacao sozinho kkkk