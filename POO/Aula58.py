# Entendendo self em classes em python
# Classe- Molde (geralmente sem dados)
# Instância da class (objeto) - tem os dados
# Uma classe pode gerar varias outras instâncias
# Na classe o self é a própia instância.
# Self = eu mesmo 

class Carro:
    def __init__(self, nome):
        self.nome = nome

    def acelerar(self):
        print(f'{self.nome} está acelerando...')


fusca = Carro('Fusca')
fusca.acelerar()
Carro.acelerar(fusca)


celta = Carro(nome='Celta')
celta.acelerar()
Carro.acelerar(celta)
