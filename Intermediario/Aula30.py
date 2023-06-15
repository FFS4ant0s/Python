'''
Funções  (def) em  python - global  variavel - (PARTE 4)
'''

variavel = 'valor'

def func():
    print(variavel)

def func2():
    variavel = 'Outro valor'
    print(variavel)

def func3():
    print(variavel)

func()
func2()
func3()