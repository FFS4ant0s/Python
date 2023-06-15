import os
import shutil

def copia_diretorio(caminho_fonte, caminho_destino):
    for root, dirs, files in os.walk(caminho_fonte):
        for dir in dirs:
            pasta_fonte = os.path.join(caminho_fonte)
            pasta_destino = os.path.join(caminho_destino, os.path.relpath(pasta_fonte, caminho_fonte)) 
            # é uma função que retorna um caminho relativo de um arquivo ou diretório em relação a um diretório de início especificado.
            os.makedirs(pasta_destino, exist_ok=True) 
            # é uma função que cria um diretório (ou vários diretórios) recursivamente no caminho especificado.
            for file_ in files:
                pasta_fonte = os.path.join(root, file_)
                pasta_destino = os.path.join(caminho_destino, os.path.relpath(pasta_fonte, caminho_fonte))
                shutil.copy2(pasta_fonte, pasta_destino)

            
copia_diretorio(r'C:\\Users\FERNANDO\dev\python\Pythonproject\Exemplos\exemplo.txt',
                r'C:\Users\FERNANDO\dev\python\Pythonproject\Exemplos\exemplo1.txt')