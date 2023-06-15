# __new__ e __init__ em classes python
# __new__ é o método responsável por criar e retornar o novo objeto.
# Por isso, new recebe cls.
# __new__ ! DEVE retornar o novo objeto!
#__init__ é o método responsável por inicializar a instância. Por isso init recebe self.
#__init__ !NÃO DEVE retornar nada (None)!
# Object é a super classe de uma classe

class A:
    def __new__(cls, *args, **kwargs):
        inst = super().__new__(cls)
        return inst

    def __init__(self, x):
        self.x = x
        print('SOU O INIT')

    def __repr__(self):
        return(A)


a = A(123)
print(a.x)  