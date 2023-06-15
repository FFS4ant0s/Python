# os.walk
# os.walk é uma função que permite percorrer uma estrutura de diretórios de 
# maneira recursiva. Ela gera um sequência de tuplas, onde cada tupla pussui
# três elementos: o diretório atual(root), uma lista de subdiretorios(dirs) 
# e uma lista dos arquivos do diretório atual(files).
import os
from itertools import count

caminho = os.path.join(r'C:\Users','FERNANDO','dev','python','Pythonproject','Exemplos')
counter = count()

for root, dirs, files in os.walk(caminho):
    the_counter = next(counter)
    print(the_counter ,'Pasta atual', root)

    for dir_ in dirs:
        print('  ', the_counter, 'Dir:', dir_)

    for file_ in files:
        caminho_completo = os.path.join(root, file_)
        print('  ', the_counter, 'File:', file_)
        
        # NÃO FAÇA ISSO (VAI APAGAR TUDO DA PASTA.)
        # os.unlink(caminho_completo_arquivo)