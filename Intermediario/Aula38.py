'''
Iteradores e Geradores
'''

nome = 'Fernandinho'
iterador = iter(nome)
gerador = (letra for letra in nome)

print(next(gerador))
print(next(gerador))
print(next(gerador))
print(next(gerador))
print(next(gerador))

print('Olha o  for ')

for letra in gerador:
    print(letra)
