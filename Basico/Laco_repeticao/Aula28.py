'''
Funções (def) em python - return - Aula 16 (PARTE 2)
'''

n1 = float(input('digite um número'))
n2 = float(input('digite um número'))
n3 = float(input('digite um número'))

def divisao(n1, n2, n3):
    print(n1 + n2 + n3)

divide = divisao(n1, n2, n3)

print(divide)

def dumb():
    return ('nando reis')
var = dumb()

print(var)