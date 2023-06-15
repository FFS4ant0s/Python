# Herança Múltipla - Python Orientado a Objetos
# Quer dizer que no Python, uma classe pode estender várias outras classes.
# Herança simples :
# Animal -> Mamifero -> Humano -> Pessoa -> Cliente 
# Herança múltipla e mixins 
# Log -> FileLog
# Animal -> Mamifero -> Humano -> Pessoa -> Cliente
# Cliente(Pessoa, FileLog)
#
# Python 3 usa c3 superclass linearization para gerar mro(method relucion order). 
# Você não precisa estudar isso.
# https://en.wikipedia.org/wiki/C3_linearization
#
# Para saber a ordem de chamada do métodos
# Use o método de classe Classe.mro()
# Ou o atributo __mro__ (Dunder - Double Underscore) 
#
class A: 
    pass

    def quem_sou(self):
        print('A')
    
class B(A): 
  """   pass

    def quem_sou(self):
        print('B') """

class C(A): 
    """ pass

    def quem_sou(self):
        print('C')
 """
class D(B, A): 
   """  pass

    def quem_sou(self):
        print('D')
 """
d = B()
d.quem_sou()

print(d)