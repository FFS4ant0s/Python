'''
Dicionário em python
'''
import copy

d1 = {
    'chave1' : 'valor',
     'chave2': 'Outro valor',
    'chave3' : 'Tupla',
}

del d1['chave1'] #deleta  o termo  selecionado do dicionario.(no caso 'chave1').
print(d1.get('chave3'))

for k, v in d1.items():
    print(k, v)

clientes = {       # Dicionários dentro de dicionários
    'cl1' : {
        'nome' : 'Luiz',
        'sobreome' : 'Otavio',
    },
    'cl2' : {
        'nome' : 'Lucas',
        'sobreome' : 'Otavio',
    },
    'cl3' : {
        'nome' : 'amanda',
        'sobreome' : 'souza',
    },

}
for clientes_k, clientes_v in clientes.items():     # Interação de dicionários dentro de dicionários.
    print(f'Exibindo {clientes_k}')
    for dados_k, dados_v in clientes_v.items():
        print(f'\t{dados_k} = {dados_v} ')


d1 = {}