
## Aprendendo o padrão orientado a objetos do python

class Player():
    def __init__(self, initChar, initClasse, initSkill):
        self.nome = initChar
        self.classe = initClasse
        self.habilidade = initSkill


char1 = Player('Reyna','Duelista','Frenesi')
char2 = Player('Astra','Controlador','Véu cósmico')
print(char1.habilidade,"\\" ,  char2.habilidade) ## -> Teste para printar no terminal as informações do objeto