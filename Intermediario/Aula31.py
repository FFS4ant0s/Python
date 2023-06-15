'''
Função lambda em python
'''

def funcao(arg,arg2):
    return arg * arg2
var = funcao(2,2)
print(var)


a = lambda x, y: x * y
print(a(2,2))

lista = [
    ['P1', 13],
    ['P2', 14],
    ['P3', 8],
    ['P4', 9],
    ['P5', 2],
         ]



print(sorted(lista, key=lambda i: i[0],reverse=True))
print(lista)