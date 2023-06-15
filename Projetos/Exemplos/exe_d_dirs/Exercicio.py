"""
    Suponha que você tenha uma pasta com vários arquivos e subpastas
e queira percorrer essa estrutura de pastas para encontrar todos os arquivos 
com uma determinada extensão, como ".txt".
    Escreva um programa em Python que realiza essa tarefa usando a biblioteca "os"
"""
import os 

def encontra_arquivos(tipo_arquivo, diretorio):
    for root, dirs, files in os.walk(diretorio): 
        for file_ in files:
            if file_.endswith(tipo_arquivo):
                print('Aquivos em formato', tipo_arquivo, ':' ,os.path.join(root, file_))
    


encontra_arquivos('.json', r"C:/Users/FERNANDO/dev/python/Pythonproject/Exemplos")
d = os.path.join(r"C:/Users/FERNANDO/dev/python/Pythonproject/Exemplos")
print('--'*30)
print(d)