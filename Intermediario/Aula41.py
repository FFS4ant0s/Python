'''
Combinations, Permutations e Product - Itertools
Combinação - Ordem não importa
Permutação -  Ordem importa
Ambos não repetem valores únicos
Produto - Ordem importa e repete valores únicos
'''
# Pegando combinções poossíveis
from itertools import combinations, permutations, product

guys = {'luiz', 'andre', 'carlos', 'raissa'}
print(guys)

def lin():
    print('=-='*30)

for grupo in combinations(guys,  2):
    print(grupo)
lin()
for grupo1 in permutations(guys, 2):
    print(grupo1)
lin()
for grupo2 in product(guys, repeat= 2):
    print(grupo2)
