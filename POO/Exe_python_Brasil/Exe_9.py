"""Classe Ponto e Retangulo: Faça um programa completo utilizando funções e classes que:

    Possua uma classe chamada Ponto, com os atributos x e y.
    Possua uma classe chamada Retangulo, com os atributos largura e altura.
    Possua uma função para imprimir os valores da classe Ponto
    Possua uma função para encontrar o centro de um Retângulo.
Você deve criar alguns objetos da classe Retangulo.
    Cada objeto deve ter um vértice de partida,
por exemplo, o vértice inferior esquerdo do retângulo, que deve ser um objeto da classe Ponto.
    A função para encontrar o centro do retângulo deve retornar o valor para um objeto do tipo ponto
que indique os valores de x e y para o centro do objeto.
    O valor do centro do objeto deve ser mostrado na tela
Crie um menu para alterar os valores do retângulo e imprimir o centro deste retângulo.
"""

class Ponto():
    def __init__(self, x : float, y : float):
        self.x = x
        self.y = y
    
    def mostra_dados(self):
        print('--'*30)
        print('Ponto x:', self.x, '\nPonto y:', self.y)
        print(f'O centro do retangulo é o ponto ({self.x} , {self.y})')

class Retangulo(Ponto):
    def __init__(self, largura : float, altura : float):
        self.largura = largura
        self.altura = altura

    def centro_retangulo(self):
        p1 = self.largura/2
        p2 = self.altura/2
        self.x = p1
        self.y = p2
        

    def altera_dados(self):
        l = float(input('Digite o valor da largura: '))
        a = float(input('Digite o valor da Altura: '))
        self.largura = l
        self.altura = a


if __name__ == '__main__':
    p = Retangulo(6, 4)
    p.centro_retangulo()
    p.mostra_dados()
    p.altera_dados()
    p.centro_retangulo()
    p.mostra_dados()
    