# csv.reader e csv.DictReader
# csv.reader lê o CSV em formato de lista
# csv.DictReader lê em formato de dicionário
import csv
from pathlib import Path

CAMINHO_CSV = Path(__file__).parent / 'arq1.csv'

# with open (CAMINHO_CSV, 'r') as arquivo:   # Lendo em formato de lista
#     leitor = csv.reader(arquivo) # =--------->
    
#     for linha in leitor:
#         print(linha)

with open (CAMINHO_CSV, 'r') as arquivo:   # Lendo em formato de Dicionario
    leitor = csv.DictReader(arquivo)   # ----->
    
    for linha in leitor:
        print(linha['Nome'], linha['Sexo'])