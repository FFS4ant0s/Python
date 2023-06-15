# Teoria: python Special Methods, Magic Methods ou Dunder Methods.
# Dunder = Double Underscore = __dunder__
# Antigo e útil: https://rszalski.github.io/magicmethods/
# https://docs.python.org/3/reference/datamodel.html#specialnames
# __lt__(self,other) - self < other  # Checar se é maior.
# __le__(self,other) - self <= other # Checar se é maior ou igual.
# __gt__(self,other) - self > other  # Checar se é menor.
# __ge__(self,other) - self >= other # Checar se é menor ou igual. 
# __eq__(self,other) - self == other # Checar se é igual.
# __ne__(self,other) - self != other # Checar se é diferente.
# __add__(self,other) - self + other # Soma.
# __sub__(self,other) - self - other # Subitração.
# __mul__(self,other) - self * other # Multiplicação.
# __truediv__(self,other) - self / other # Divisão.
# __neg__(self) - -self # Inverter para negativo.
# __str__(self) - str # Chamar a str('string de um metodo'.).
# __repr__(self) - str # Chamar a representação.

class Ponto():
    def __init__(self, x, y, z= 'string'):
        self.x = x
        self.y = y
        self.z = z

    def __str__(self):  # 
        return f'({self.x}),({self.y})'


    def __repr__(self):   # para desenvolvedores
        class_name = type(self).__name__  
        return f'{class_name}(x = {self.x!r}), (y = {self.y!r}, (z = {self.z!r})'




p1 = Ponto(1, 2)
p2 = Ponto(978, 876)
print(p1)
print(repr(p2))
print(f'{p2!r}')