from pathlib import Path

caminho_projeto = Path()
# print(caminho_projeto.absolute())


caminho_arquivo = Path(__file__)
# print(caminho_arquivo)

ideias = caminho_arquivo.parent / 'ideias'
# print(ideias / 'arquivo.txt')

# print(Path.home())

arquivo = Path.home() / 'dev' / 'python' / 'Pythonproject' / 'arq.txt'
#arquivo.touch() # Criando um novo arquivo.
# print(arquivo)
# #arquivo.unlink() # apagando arquivo
# arquivo.write_text('Olá pessoas') # Escrevendo dentro do arquivo.
# print(arquivo.read_text()) # lendo arquivo
arquivo.unlink() # apagando arquivo
# with open(caminho_arquivo, 'a+') as file:
#     file.write('Uma linha\n')
#     file.write('Outra linha\n')

# print(caminho_arquivo.read_text())