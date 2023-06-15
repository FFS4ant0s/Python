# Formatando valores com modificadoress - Aula 5

# :s - Texto (strings)
# :d - Inteiros (int)
# :f - Números com ponto flutuante (float)
# :.(número)f - Quantidade de casas  decimais (float)
# : (Caractere)(< ou > ou ^)(Quantidade)(Tipo - s,d ou f)

# > - ESQUERDA
# < - DIREITA
# ^ - CENTRO

num_1 = 1
print(f'{num_1:0>10}')

num_2 = 1150.6778
print(f'{num_2:.2f}')

nome = 'nando'
print(nome.split()) #[' nome '] coloca cada string entre colchetes e aspas.
print(nome.lower()) #tudo minusculo
print(nome.upper()) #tudo maiusculo
print(nome.title()) #Primeiras letras maiusculas
print(nome.isalpha()) #True se todos os caracteres da string forem alfabéticos


n = input('Digite uma frase: ')

while not n.isalpha():
    print('Uma frase seu animal sem números.')
    n = input('Digite uma frase: ')

else:
    print('Acabou')