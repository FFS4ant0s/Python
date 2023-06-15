'''
Sets em python # Não aceitam elementos duplicados!
.add() = Adiciona, update() = intera cada elemento , union() or | = une os elementos
intersection & (apenas os elementos presentes nos dois sets),
difference - (apenas os elementos q estejam no set  da esquerda),
symmetric_difference ^ = Elementos q estão  nos dois sets mass não estão em ambos.
'''


s1 = {1,2,3,3,2,1,8}
s2 = {1,2,3,4,5,6}
s3 = s1 & s2
s4 = s1 | s2
s5 = s1 - s2
s6 = s1 ^ s2
s1.update()
s2.add(10)
print(s1)
print(s2)
print(s3)
print(s4)
print(s5)
print(s6)