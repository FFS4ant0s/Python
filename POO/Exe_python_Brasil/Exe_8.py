"""
  Classe Macaco: Desenvolva uma classe Macaco,
que possua os atributos nome e bucho (estomago) e pelo menos os métodos comer(), verBucho() e digerir(?).
  Faça um programa ou teste interativamente, criando pelo menos dois macacos,
alimentando-os com pelo menos 3 alimentos diferentes e verificando o conteúdo do estomago a cada refeição.
   Experimente fazer com que um macaco coma o outro.
   É possível criar um macaco canibal ?
"""

class Macaco:
    def __init__(self, nome, estomago):
        self.nome = nome
        self.estomago = estomago
    

    def comer(self,):
        while True:    
            comida = input('O que o macaco vai comer? ')
            print(f'O Macaco esta comendo {comida}...')
            self.estomago.append(comida)
            decisao = input('O macaco vai continuar comendo?(S/N) ')
            if decisao in 'Nn':
                break
            elif decisao in 'Ss':
                ...
   
    def digerir(self):
        print('-'*40)
        print('O macaco está digerindo...')
    
    def verBucho(self):
        cont = 1
        for i in self.estomago:
            print(f'Alimento {cont}º: {i}')
            cont += 1

if __name__ =='__main__':
    m1 = Macaco('jao', [] )
    m2 = Macaco('Luiz', [m1])
    m1.comer()
    m2.verBucho()