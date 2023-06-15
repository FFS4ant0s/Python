'''
Funções  (def) em  python  - *args  **kwargs - (PARTE 3)
'''


def func(*args, **kwargs):
    args = list(args)
    print(*args,sep='-')
    args[0] = 20
    print(args[-1])
    print(*args)
    nome = kwargs.get('nome') # get retorna o valor 
    sobrenome = kwargs.get('sobrenome')
    print(nome, sobrenome)



lista = [1,2,3,4]
lista2 = [10,20,30,40]
func(*lista, *lista2, nome='Luiz', sobrenome='Miranda')
