import json 
'''
Json não suporta funçoes ou classes
encondig = 'utf8' --> Acentos
'''
pessoa = { 
    'Nome' : 'Fernando',
    'Sobrenome': 'Miranda ',
    'endenreços ' : [
       {'rua' : 'R1', 'numero': 32},
       {'rua' : 'R2', 'numero': 55},
    ],
    'altura' : 1.8,
    'numeros_preferidos' : (2, 4, 6, 8, 10),
    'dev' : True,
    'nada' : None,
}

with open('aula117.json', 'w+' , encoding='utf8') as file: # Criando um arquivo em Json 
    json.dump(pessoa, file)
    

with open('aula117.json', 'r', encoding='utf8') as file: # abra e leia o arquivo !!
    pessoa = json.load(file)
    print(pessoa['Nome'])
