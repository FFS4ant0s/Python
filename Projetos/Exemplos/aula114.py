# os.listdir para navegar em caminhos
# caminho = c:/Users/FERNANDO/dev/python/Pythonproject/Exemplos
import os

caminho = os.path.join(r'C:\Users','FERNANDO','dev','python','Pythonproject','Exemplos')

for pasta in os.listdir(caminho):
    caminho_completo_pasta = os.path.join(caminho, pasta)
    print(pasta)

    if not os.path.isdir(caminho_completo_pasta):
        continue

    for imagem in os.listdir(caminho_completo_pasta):
        print('  ', imagem)