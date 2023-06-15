"""
Map == manipulação de dicionario
"""

from Dados import produtos,lista,pessoas

precos = map(lambda p: round(p['preco']*2,10), produtos)

for p in precos:
    print(p)

nomes = map(lambda g: g['nome'], pessoas)

for n in nomes:
    print(n)

lst1 = map(lambda l: l*2, lista)
print(list(lst1))

x = [i*2 for i in lista]
print(x)