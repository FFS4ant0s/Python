# Escopo da classe e de métodos da classe

class Animal:
    def __init__(self, nome):
        self.nome = nome
    def comendo(self):
        print(f'{self.nome} está comendo.')

leao = Animal(nome='leao') # assim você pode usar a istancia em qualquer lugar da CLASSE
leao.comendo()
