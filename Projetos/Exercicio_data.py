# Maria pegou um empréstimo de 1.000.000
# para realizar o pagamento em 5 anos 
# A data em que ela pegou o emprestimo foi 20/12/2020
# O vencimento de cada parcela é no dia 20 de cada mês.
# - Crie a data do empréstimo
# - Crie a data do final do empréstimo
# - Mostre todas as datas de vencimento e o valorde cadad parcela
from datetime import datetime, timedelta

from dateutil.relativedelta import relativedelta

fmt = '%d/%m/%Y'
data_inicio = datetime.strptime('20/02/2022', fmt)
valor_emprestimo = 1_000_000
parcelas = valor_emprestimo/(5*12)
data_fim = (data_inicio + relativedelta(years=5))
print(f'Data inicial: {data_inicio} \nData final: {data_fim}')

while data_inicio < data_fim:
    data_inicio += relativedelta(months=1)
    print(f'Data de vencimento: {data_inicio}  /  Valor da parcela: {parcelas:.2f} R$')
