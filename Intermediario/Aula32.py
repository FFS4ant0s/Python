'''
Tuplas em python = Não podem ser alteradas!!
'''

t1 = 1,2,3,'a','Nandin'
print(t1[2::2])

for v in t1:
    print(v)

t2 = 1,3,'luiz',5,'nando'
t3 = 4,5,76,78,
t4 = t2 + t3
print(t4)

*_ ,n1,n2,n3, = t4
print(*_)

#covertendo em lista
t5 = 1,2,3,4,5
t5 = list(t5)
t5[1] = 2000
print(t5)