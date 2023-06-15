"""
listas em python
fatiamento
.append (Inserir um valor ao final), insert(inserir em um determinado lugar), pop(Deleta o último elemento da lista),
del(Deletar), clear, extend, min(minimo), max(maximo),range(todos os  números até.)
"""
#ls1 = [5,6,7,8]
#ls2 = [1,2,3,4]

#ls1.append()
#ls2.pop()
#del(ls2[:])
#print(max(ls2))
#print(min(ls1))

secreto =  'perfume'
dgts = []

while True:
    letra = input('Digite uma  letra: ')

    if len(letra) > 1:
        print('por favor digite apenas uma  letra.')
        continue

    dgts.append(letra)

    if letra in secreto:
        print('essa letra existe na palavra. ')

    else:
        print('Letra não existe.')
        dgts.pop()

    letra_secreta = ''

    for secreto_temp in secreto:
        if secreto_temp in dgts:
             letra_secreta += secreto_temp

        else:
            letra_secreta += '*'
