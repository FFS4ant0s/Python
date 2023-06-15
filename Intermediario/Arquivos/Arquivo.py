"""
Criando, lendo, escrevendo e apagando arquivos
"""

"""
w+ = Criar e escrever linhas em um arquivo 
r = Ler linhas de um arquivo
a+(append mode) = adicionar coisas no arquivo ao final. 
"""

def lin():
    print('-'*42)

file = open('../pythonProject/abc.txt', 'w+') #abrir um arquivo para leitura e escrita!!!(Você pode editar o arquivo.)
file.write('Linha 1\n') #Criando linhas do arquivo !!
file.write('Linha 2\n') #Criando linhas do arquivo !!
file.write('Linha 3\n') #Criando linhas do arquivo !!

file.seek(0, 0)  # Volte ao inicio do arquivo!
print('lendo linhas:')
print(file.read())  # Leia todo o arquivo
lin()

file.seek(0,0)
print(file.readline(), end='') # Lendo cada linha do arquivo!!
print(file.readline(), end='') # Lendo cada linha do arquivo!!
print(file.readline(), end='') # Lendo cada linha do arquivo!!

lin()
file.seek(0, 0)  # Volte ao inicio do arquivo!
for linha in file.readlines():
    print(linha,end='')


file.close()  # Fechando o arquivo!!

with open('../pythonProject/abc.txt', 'w+') as file:
    file.write('Linha 1\n')  # Criando linhas do arquivo !!
    file.write('Linha 2\n')  # Criando linhas do arquivo !!
    file.write('Linha 3\n')  # Criando linhas do arquivo !!

    file.seek(0, 0)  # Volte ao inicio do arquivo!
    print(file.read())  # Leia todo o arquivo
