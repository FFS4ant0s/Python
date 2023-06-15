"""
    Classe carro: Implemente uma classe chamada Carro com as seguintes propriedades:

    Um veículo tem um certo consumo de combustível (medidos em km / litro)
 e uma certa quantidade de combustível no tanque.
    O consumo é especificado no construtor e o nível de combustível inicial é 0.
    Forneça um método andar( ) que simule o ato de dirigir o veículo por uma certa distância,
reduzindo o nível de combustível no tanque de gasolina.
    Forneça um método obterGasolina( ), que retorna o nível atual de combustível.
    Forneça um método adicionarGasolina( ), para abastecer o tanque. 
"""

class Carro:
    def __init__(self, consumo : float = 10, tanque : int = 0, nome : str = 'Garou'):
        self.consumo = consumo
        self.tanque = tanque
        self.nome = nome

    def mostra_dados(self):
        print('--'*30)
        print('Carro:', self.nome, '\nConsumo:', self.consumo, 'km/l', '\nTanque:', self.tanque, 'Litros restantes.' )
        print('=='*30)

    def andar(self):
        while True:
            anda = float(input('Quantos kilometros deseja andar: '))
            lt = anda/self.consumo
            confere = self.tanque - lt
            if confere < 0:
                print('--'*30)
                print('Seu carro não tem gasolina o suficiente para andar tudo isso. :() ')
                print('--'*30)
            else: 
                self.tanque -= lt               
                break
        print(f'Andando {anda}KM....')

    
    def ver_tanque(self):
        print('Tanque:', self.tanque, 'Litros.')

    def abastecer(self):
        abastece = float(input('Quantos litros deseja abastecer: '))
        nv_tanque = abastece + self.tanque
        self.tanque = nv_tanque

if __name__ == '__main__':
    car = Carro()
    car.mostra_dados()
    car.abastecer()
    car.mostra_dados()
    car.ver_tanque()
    car.andar()
    car.mostra_dados()