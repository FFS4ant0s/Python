# CSV (Comma Separated values - Valores separados por vírgula.)          
# É um formato de arquivo que armazena dados em forma de tabela, onde cada linha 
# representa uma linha da tabela e as colunas são separadas por vírgulas.
# Ele é amplamente utilizado para transferir dados entre sistemas de diferentes
# plataformas, como por exemplo, para importar ou exportar dados para umas planilha (Google Sheets, Excel, LibbreOffice Calc)
# ou para uma base de dados.  
# Um arquivo CSV geralmente te a extensão ".csv" e pode ser aberto em um editor de texto e/ou planilha eletronica.
# Um exemplo de um arquivo CSV pode ser:
# Nome,Idade,Endereço
# Luiz Otávio,32,"Av Brasil, 21, Centro"
# João da Silva,55, "Rua 22, 44, Nova Era"
# A primeira linha do arquivo define os nomes das colunas da, enquanto  as
# linhas seguintes contêm os valores das linhas, separados por vírgulas.
# Regras simpoles do CSV
# 1 - Separe os valores das colunas com delimitador único (,)
# 2 - Cada registro deve estar em uma linha
# 3 - Não deixar linhas ou espaçços sobrando
# 4 - Use o caractere de escape (") quando o delimitador aparecer

from pathlib import Path

arquivo = Path.home() / 'dev' / 'python' / 'Pythonproject' / 'arq1.csv'
arquivo.touch()
dados = """Nome,Idade,Sexo,Salário
Fernando,22,Masculino,5.000
João da Silva,55,Masculino,10.000
Luiz Otávio,32,Masculino,20.000
Raissa,20,Feminino,1.000
"""
arquivo.write_text(dados)
print(arquivo.read_text())