#Outras formas de fazer o comando!!!!

nome = 'fernando fernandes'
idade = 22
altura = 1.77
e_maior= idade > 18
peso= 85
imc= peso/(altura**2)

print(nome, 'tem', idade, 'anos de idade e seu imc é ',imc )
print(f'{nome} tem {idade} anos de idade e seu imc é {imc:.2f}') #arrendondado o valor de imc
print('{} tem {} anos e seu imc é {}'.format(nome,idade,imc)) #não usa tanto as virgulas leitura mais limpa !!!!

