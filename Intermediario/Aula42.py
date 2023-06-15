from itertools import groupby

alunos = [
    {'nome': 'luiz', 'nota': 'A'},
    {'nome': 'leticia', 'nota': 'B'},
    {'nome': 'luie', 'nota': 'A'},
    {'nome': 'lucas', 'nota': 'B'},
    {'nome': 'luizao', 'nota': 'C'},
    {'nome': 'luiza', 'nota': 'C'}
]
alunos.sort(key=lambda item: item['nota']) #ordenar por notas iguais

for a in alunos:
    print(a)

alun_agrup = groupby(alunos, lambda item: item ['nota'])

for a2 in alun_agrup:
    print(a2)