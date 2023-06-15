from Aula61 import *

with open('Carros.json', 'r', encoding='utf8') as file: # abra e leia o arquivo !!
   carro = json.load(file)
   print(carro['ano'])

carrinho2 = Carro(carro['marca'], carro['ano'], carro['modelo'])
print(carrinho2.marca) 