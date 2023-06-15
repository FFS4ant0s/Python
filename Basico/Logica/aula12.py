"""
Operadores Lógicos - Aula 4
and (e), or(ou), not(inversão), in(contém) e not in (não contem)
"""
a = 2
b = 3
c = 5
d = 6

if not b > a and c > d: #se b > a e c > d
  print('C é maior que a e b.')

elif b > a or d == c: #se b > a ou d == c
  print('D é maior que todos.')

else :
  print('a ou b são maiores que c.')

name = 'Luiz'

if 'u' in name: #se 'u' tiver em name
  print('Existe u no seu name.')

else:

  print("não existe u no seu name.")





