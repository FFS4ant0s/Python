from datetime import datetime, timedelta

from dateutil.relativedelta import relativedelta

print('=='*30)
print('agenda'.upper().center(60))
print('=='*30)
num_horas_total = 132.5
num_horas_visto = (132.5*0.4)
num_horas_restante = num_horas_total - num_horas_visto
print(f'Você precisa ver {num_horas_restante} horas de aula.')
print('--'*30)
dia_atual = datetime.now()
dia_final = dia_atual + relativedelta(months=3)
print(f'Dia inicial: {dia_atual}')
print('--'*30)
print(f'Dia final : {dia_final}')
print('--'*30)

dias = dia_final - dia_atual
print(f'Total de dias restantes: {dias}')
print('--'*30)
dias_estudados = (92/2) + 2
print(f'Dias estudados (seg/quinta): {dias_estudados} days.')
print('--'*30)
print('2 horas ao dia ou 9 aulas ao dia é o mínimo.')
print('--'*30)