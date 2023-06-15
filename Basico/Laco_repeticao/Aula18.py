"""
while em python - Aula 7
utilizado para realizar ações enquanto uuma condição for verdadeira.

Reequisitos: entender condições e operadores.

while = enquanto
"""

x = 0


while True:
    print()
    num_1 = input('Digite um número: ')
    num_2 = input('Digite outro número: ')
    operator = input('Digite um operador: ')

    if not num_1.isnumeric() or not num_2.isnumeric():
        print('isso não é um número.')

    num_1 = int(num_1)
    num_2 = int(num_2)

    # + - / *

    if operator == '+':
       print(num_1 + num_2)
       break

    elif operator == '-':
        print(num_1 - num_2)
        break
    
    elif operator == '/':
        print(num_1/num_2)
        break

    elif operator == '*':
        print(num_1 * num_2)
        break