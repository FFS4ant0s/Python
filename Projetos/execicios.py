"""
Classe Bola: Crie uma classe que modele uma bola:

Atributos: Cor, circunferência, material
Métodos: trocaCor e mostraCor
"""

class Bola:
    def __init__(self, Cor : str , circunferencia : float, material : str):
        self.Cor = Cor
        self.circunferencia = circunferencia
        self.material = material

    def trocaCor(self):
        nv_cor = str(input('Nova cor: '))
        self.Cor = nv_cor
        return self.Cor 

    
    def mostraqcor(self):
        print(f'{self.Cor}')

if __name__ == '__main__':
    b = Bola('azul', 1.77, 'aço')
    b.mostraqcor()
    print('--'*30)
    b.trocaCor()
    print('--'*30)
    b.mostraqcor()


