import re

# Abre o arquivo e lê o conteúdo
with open('dados_freela.txt', 'r') as arquivo:
    conteudo = arquivo.read()

# Define a expressão regular para encontrar números inteiros
regex = r'\d+'

# Encontra todos os números inteiros no conteúdo
numeros = re.findall(regex, conteudo)

# Imprime os números encontrados
print(numeros)