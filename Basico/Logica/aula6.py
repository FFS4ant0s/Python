nome = 'fernando fernandes' #string
idade = 22 #int
altura = 1.77 #float
e_maior = idade > 18 #bool
peso = 85
imc = peso / (altura ** 2)
print( nome,'tem ',idade,'anos de idade e seu imc é', imc )
print(f'{nome} tem {idade} anos de idade e seu imc é {imc:.2f}')