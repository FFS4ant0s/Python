"""
Compreensões de listas - Otimização(Performasse) - diminuição de codigo.
"""


def lin():
    print('--' * 30)


x = [1, 2, 3, 4, 5, 6, 7, 8, 9]
ex1 = [i for i in x]
print(ex1)

lin()

ex2 = [v * 2 for v in x]
print(ex2)

lin()

ex3 = [(v, v2) for v in x for v2 in range(3)]
print(ex3)

lin()

x2 = ['Raissa', 'Julia', 'Fernanda']
ex4 = [v.replace('a', '@').upper() for v in x2]
print(ex4)

lin()

T = (
    ('chave', 'valor'),
    ('chave2', 'valor2'),
)

ex5 = [(t1, t2) for t2, t1 in T]

print(ex5)
ex5 = dict(ex5)
print(ex5['valor'])

lin()

L = list(range(100))
ex6 = [l for l in L if l % 10 == 0 if l % 8 == 0]
print(ex6)
lin()
ex7 = [l if l % 10 == 0 else 'Não' for l in L ]
print(ex7)