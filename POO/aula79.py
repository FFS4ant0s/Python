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
    def __init__(self, x, y):
        self.x = x
        self.y = y
       

    def __repr__(self):   # para desenvolvedores
        class_name = type(self).__name__  
        return f'{class_name}(x = {self.x!r}), (y = {self.y!r})'

    def __add__(self, other):
        novo_x = self.x + other.x
        novo_y = self.y + other.y
        return Ponto(novo_x, novo_y)
    
    def __gt__(self, other):
        resultado_self = self.x + self.y
        resultado_other = other.x + other.y
        return resultado_self > resultado_other


if __name__ == '__main__':
        p1 = Ponto(1, 2)
        p2 = Ponto(978, 876)
        p3 = p1 + p2
        print(p3)
        print('P1 é maior que p2', p1 > p2)
        print('P2 é maior que p1', p2 > p1)