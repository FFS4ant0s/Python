"""
Classe Quadrado: Crie uma classe que modele um quadrado:

Atributos: Tamanho do lado
Métodos: Mudar valor do Lado, Retornar valor do Lado e calcular Área;
"""

class Quadrado:
    def __init__(self, tam_lado : float):
        self.tam_lado = tam_lado

    def mudar_valor_lado(self):
        nv_lado = float(input('Novo valor do Lado: '))
        self.tam_lado = nv_lado
        return self.tam_lado
    
    def retorna_valor_lado(self):
        ant_lado = x
        self.tam_lado = ant_lado
        return self.tam_lado

    def mostra_lado(self):
        print(f'O valor do lado é: {self.tam_lado}')

    def cal_area(self):
        area = (self.tam_lado)**2
        print(f'A área do quadrado é: {area}')

if __name__ == '__main__':
    x = 2
    q = Quadrado(x)
    q.mostra_lado()
    q.mudar_valor_lado()
    q.mostra_lado()
    q.retorna_valor_lado()
    q.mostra_lado() 
    q.cal_area()    