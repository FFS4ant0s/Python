class Carro:
    def __init__(self, nome):
        self.nome = nome 
        self._motor = None
        self._fabricante = None
    
    @property
    def motor(self):
        return self._motor

    @motor.setter
    def motor(self, valor):
        self._motor = valor
    
    @property
    def fabricante(self):
        return self.fabricante

    @fabricante.setter
    def fabricante(self, valor):
        self.fabricante = valor
class Motor:
    def __init__(self, nome):
        self.nome = nome 

class Fabricante:
    def __init__(self, nome):
        self.nome = nome 
    
peugeot = Carro('peugeot')
V_tec = Motor('1.4')
champion = Fabricante('champion')

print(peugeot.nome, V_tec.nome, champion.nome)

skiline = Carro('Skiline')
V_tec = Motor('V-tec')
nissan = Fabricante('Nissan')

print(skiline.nome, V_tec.nome, nissan.nome)