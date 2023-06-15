"""
Orientação Orientada a objeto
"""

# 1 class - Classes são moldes para criar novos objetos.
# 2 As clases geram novos objetos (instâncias) que podem ter seus próprios atributos e métodos.
# 3 Os objetos gerados pela classes podem usar seus dados internos para realizar varias ações.
# 4 Por convenção, usamos PascalCase para nome de classes.

string = 'luiz'
print(string.upper())
print(isinstance(string, str)) # isinstace = verificar se ('String') é uma stancia de str

class Pessoa: # Sempre uma nova palavra com letra maiuscula
   def __init__(self, nome, sobrenome):  # Inicializa os atributos da classe !!!!
       self.nome = nome
       self.sobrenome = sobrenome

p1 = Pessoa('Luiz','Fernando')
#p1.nome = 'Luiz'
#p1.sobrenome = 'Otavio'

p2 = Pessoa('Maria', 'Fernanda')
#p2.nome = 'Luiza'
#p2.sobrenome = 'Oliveira'
"""
Observe q os atributos foram substituidos !!!!
"""
print(p1.nome)
print(p1.sobrenome)
print(p2.nome)
print(p2.sobrenome)