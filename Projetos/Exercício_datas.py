"""
    Suponha que você tenha uma lista de datas e 
queira saber a data mais recente e a mais antiga dessa lista
"""
from datetime import datetime

datas = [
    datetime(2022, 1, 1),
    datetime(2022, 2, 1),
    datetime(2022, 3, 1),
    datetime(2022, 4, 1),
    datetime(2022, 5, 1)
]

data_max = max(datas)
data_min = min(datas)

print(f'Data min : {data_min} \nData max: {data_max}')