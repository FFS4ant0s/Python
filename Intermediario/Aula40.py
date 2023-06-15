'''
count - Itertools (Contador )
'''
from itertools import count

var = [(x, y) for (x, y) in zip('iao', 'iao')]
print(var[0][0])

cont = count(start=1, step=0.5) #step = passo

for v in cont:
    print(v)

    if v >= 10:
        break


cont2 = count(start=1, step=5)
lst = ['Nando', 'joão', 'gabriel']
lst = zip(cont2, lst)
print(list(lst))