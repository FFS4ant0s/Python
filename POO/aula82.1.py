from contextlib import contextmanager # Exeções !!!!

@contextmanager
def my_open(caminho_arq, modo):
    try:
        print('abrindo arquivo')
        arq = open(caminho_arq, modo)
        yield arq # Retorna ao gerador
    except Exception as e:
        print('ERROR', e)
    finally:
        print('fechando o arquivo')
        arq.close()


with my_open('aula150.txt', 'w') as arq:
    arq.write('Linha 1\n')
    arq.write('Linha 2\n')
    arq.write('Linha 3\n')
    print('WITH', arq)