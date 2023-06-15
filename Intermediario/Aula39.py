'''
Zip - Unindo interáveis
Zip_longest - Itertools = unindos todas as combinações.
'''

from itertools import zip_longest, count

ind = count()
cid = ['são paulo', 'Rio', 'Salvador','Brasília','Recife']
est = ['SP','RJ','BA','DF']

cid_est = zip(ind,cid,est)
print(list(cid_est))

for ind, est, cid in cid_est:
    print(ind, est, cid)