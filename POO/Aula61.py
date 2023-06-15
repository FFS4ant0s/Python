# Exercício - Salve sua classe em JSON
# Salve os dados da sua classe em JSON
# e depois crie novamente as instâncias
# da classe com os dados salvos
# Faça em arquivos separados.
import json

class Carro:
    def __init__(self, marca, ano, modelo):
        self.marca = marca
        self.ano = ano
        self.modelo = modelo

carrinho = Carro('peugeot', 2010, '207')
print(f'Carro da marca {carrinho.marca}, do ano {carrinho.ano}, seu modelo é {carrinho.modelo}')
d = vars(carrinho)

with open('Carros.json', 'w+' , encoding='utf8') as file: # Criando um arquivo em Json 
    json.dump(d, file)

