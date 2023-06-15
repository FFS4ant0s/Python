"""
    Suponha que você tenha uma lista de eventos, cada evento ocorrendo em uma data específica.
    Você deseja agrupar esses eventos por mês e imprimir uma lista de todos os eventos que ocorreram em cada mês.
    Além disso, você deseja calcular o número total de eventos para cada mês.
"""
from datetime import datetime

eventos = [
    ("Evento 1", datetime(2022, 1, 15)),
    ("Evento 2", datetime(2022, 1, 20)),
    ("Evento 3", datetime(2022, 2, 5)),
    ("Evento 4", datetime(2022, 3, 10)),
    ("Evento 5", datetime(2022, 3, 20)),
    ("Evento 6", datetime(2022, 4, 5)),
    ("Evento 7", datetime(2022, 4, 10)),
    ("Evento 8", datetime(2022, 5, 1)),
    ("Evento 9", datetime(2022, 5, 15)),
    ("Evento 10", datetime(2022, 6, 1))
]

eventos_por_mes = {}
total_por_mes = {}

for evento in eventos:
    mes = evento[1].strftime("%Y-%m")
    if mes not in eventos_por_mes:
        eventos_por_mes[mes] = [evento]
        total_por_mes[mes] = 1
    else:
        eventos_por_mes[mes].append(evento)
        total_por_mes[mes] += 1

# Imprima os eventos por mês e o total de eventos por mês
for mes, eventos in eventos_por_mes.items():
    print('--'*30)
    print("Eventos em", mes, ":")
    for evento in eventos:
        print("  -", evento[0])
    print('--'*30)
    print("Total de eventos em", mes, ":", total_por_mes[mes])