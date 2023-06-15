
'''
Desempacotamento
'''

lista = []

for i in range(5):
    t = str(input('Digite seu nome: '))
    lista.append(t)

n1, n2, *_ = lista

print(_)

lista = [1, 2, 3, 4, 5]
b1, b2, *b = lista
print(b1, b2)

lista = [1,2,3,4,5]
print(*lista, sep='=')