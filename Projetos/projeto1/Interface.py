import re
import json

texto = "\n\nhttps://youtube-demo-bkt.s3.amazonaws.com/Presidential-summary-Sheets-Savanna-13-725x1024.jpg\n\nhttps://youtube-demo-bkt.s3.amazonaws.com/Presidential-Summary-Sheet-Volta-Region-10-730x1024.jpg\n"

# definir a expressão regular para extrair links
regex = r"(https?://[^\s]+)"

# encontrar todas as ocorrências da expressão regular no texto
links = re.findall(regex, texto)

# criar um dicionário para os links
dicionario_links = {"links": links}

# salvar o dicionário em um arquivo JSON
with open("links.json", "w") as arquivo:
    json.dump(dicionario_links, arquivo)