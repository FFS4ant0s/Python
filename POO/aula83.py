# Funções decoradoras e decoradores com classes

class MyreprMixin:
    def __repr__(self):
        class_nome = self.__class__.__name__
        class_dict = self.__dict__
        class_repr = f'{class_nome}{class_dict}'
        return class_repr

class SuperTime:
    ...

class Time:
    def __init__(self, nome):
        self.nome = nome

    def __repr__(self):
        class_nome = self.__class__.__name__
        class_dict = self.__dict__
        class_repr = f'{class_nome}{class_dict}'
        return class_repr


class Planeta:
    def __init__(self, nome):
        self.nome = nome
    

brasil = Time('Brasil')
port = Time('Portugual')

terra = Planeta('terra')
marte = Planeta('marte')