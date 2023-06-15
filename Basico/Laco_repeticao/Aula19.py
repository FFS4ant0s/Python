"""
while (Enquanto) / else - Aula 8
Executa uma ação enquanto uma condição for verdadeira
Loop infinito -> Quando seu código
Operadores de atribuição 
= += -= *= /= //= **= %=
"""
# while (condição):

contador = 0 # Serve para garantir q o while terá um fim.
acumulador = 1 # você vai sommer em cada laço.

while contador <= 12:
    print(contador, acumulador,end=',')
    acumulador = acumulador + contador
    contador += 3

    if contador > 5 :
        break # Termina o laço  
        # continue = vai levar novamente ao começo do laço 

else:
    print('CHEGUEI NO ELSE.')