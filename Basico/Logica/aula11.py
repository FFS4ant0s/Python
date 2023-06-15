"""
Operadores Relacionais
==(igualdade) >(maior que) >=(maior que ou igual a) <(menor que) <=(menor que ou igual a) e != diferente
"""

nome = input('Qual seu nome ?')
idade = input('Qual sua idade ?')

idade = int(idade)

# Limite para pegar empréstimo
id_menor = a0
id_maior = 30

if idade >= id_menor and idade <= id_maior:
    print(f'{nome} pode pegar o empréstimo.')
else:
    print(f'{nome} Não pode pegar o empréstimo.')