## Conceitos e práticas sobre herança no python
## Bom dia mano!

class Pessoa1():
    
    def __init__(self, initNome, initSobrenome):
        self.nome = initNome
        self.sobrenome = initSobrenome
        sobrenomeOriginal = 'Kessler'
    
class Pessoa2(Pessoa1):
    def __init__(self, initNome, initSobrenome):
        super().__init__(initNome, initSobrenome)


char1 = Pessoa1('Israel','Kessler')
print(char1.nome, char1.sobrenome)

char2 = Pessoa2('Arya', char1.sobrenome)
print(char2.nome, char2.sobrenome)

'''Os conceitos e formas de obter informações que desejo dos objetos ainda não são
   concretos. Por isso, tenho que rever novamente essa aula no futuro.'''