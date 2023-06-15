"""
Split, Join, Enumerate em Python
* Split - Dividir uma string # str
* Join - Juntar uma lista # str (CADA str vai ser colocada na frente da repetição)
* Enumerate - Enumerar elementos da lista # iteráveis
"""
string = 'O Brasil é o país  do futebol, o Brasil é penta.'
lista_1 = string.split(' ')
lista_2 = string.split(',')

for valor in lista_1:
  print(f'A letra {valor} aparece {lista_1.count(valor)}x na fase. ')

string1 ='O Brasil é penta.'
string2 = '123'
lista1 = string1
lista2 = string2

print(f'{lista1.join( lista2 )}llllllllllll')

print(f'{string1.split()}')

for num in enumerate(lista1):
    print(num)

'''
* Enumerate - Enumerar elementos da lista #list

'''

lista = [
       #0    #1     #2
    ['edu','joao','luiz'], #0
    ['maria','silviaa','joana'],  #1
    ['nando','rai','hiii'], #2
]
lista1 = enumerate(lista)
print(lista1)