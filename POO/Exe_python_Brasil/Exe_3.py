"""
Classe Retangulo: Crie uma classe que modele um retangulo:

Atributos: LadoA, LadoB (ou Comprimento e Largura, ou Base e Altura, a escolher)
Métodos: Mudar valor dos lados, Retornar valor dos lados, calcular Área e calcular Perímetro;
Crie um programa que utilize esta classe. Ele deve pedir ao usuário que informe as medidades de um local.
Depois, deve criar um objeto com as medidas e calcular a quantidade de pisos e de rodapés necessárias para o local.
"""
class Retangulo:
    def __init__(self, base : float , altura : float):
        self.base = base
        self.altura = altura
    
    def mostra_lados(self):
        print('Base:', self.base, '\nAltura:', self.altura)
    
    def mudar_valor_lados(self):
        nv_altura = float(input('Novo valor da altura: '))
        self.altura = nv_altura
        nv_base = float(input('Novo valor da base: '))
        self.base = nv_base
        return self.altura, self.base
    
    def retorna_valor_lados(self):
        print('Voltando ao valor original.')
        self.base = b
        self.altura = a
        return self.base, self.altura
    
    def cal_area(self):
        area = (self.base*self.altura)/2
        print(f'A area do retangulo é: {area}')

    def cal_perimetro(self):
        perimetro = (self.base*2) + (self.altura*2)
        print(f'O perímetro do retangulo é: {perimetro}')

if __name__ == '__main__':
    b = 2
    a = 3
    r = Retangulo(b, a)
    r.mostra_lados()
    r.cal_area()
    r.cal_perimetro()
    r.mudar_valor_lados()
    r.mostra_lados()
    r.cal_area()
    r.cal_perimetro()
    r.retorna_valor_lados()
    r.mostra_lados()
