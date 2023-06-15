'''
Threads são formas de execução de processos simultaneos.
'''
from time import sleep
from threading import Thread


class Meuthread(Thread):
    def __init__(self, texto, tempo):
        self.texto = texto
        self.tempo = tempo

        super().__init__()

    def run(self):
        sleep(self.tempo)
        print(self.texto)

t = Meuthread('Thread 1', 5)
t.start()

t2 = Meuthread('Thread 2', 10)
t2.start()

t3 = Meuthread('Thread 3', 15)
t3.start()

for i in range(20):
    print(i)
    sleep(1)