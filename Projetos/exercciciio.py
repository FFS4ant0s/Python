"""
Pergunta/Tarefa:

Crie uma classe para representar uma pessoa, com os atributos privados de nome, data de nascimento e altura.
 Crie os métodos públicos necessários para sets e gets e também um método para imprimir todos dados de uma pessoa.
  Crie um método para calcular a idade da pessoa.
A data de nascimento pode ser informada como uma String (no formato 05/10/1982, por exemplo)
 e, no cálculo da idade, considere apenas o ano da data de nascimento informada.
"""
from datetime import datetime
class Pessoa:
    def __init__(self, nome, data_nasc, altura):
        self._nome = nome
        self._data_nasc = data_nasc
        self._altura = altura

    def imprimi_dados(self):
        print("Nome:", self._nome, "\nData de nascimento:", self._data_nasc, "\nAltura:", self._altura)  

    def cal_idade(self):
        ano_atual = datetime.today().year
        partes_data_nascimento = self._data_nasc.split("/")
        ano_nasc = partes_data_nascimento[2]
        anos = ano_atual - int(ano_nasc)
        print("A pessoa tem", anos, "anos.")

    def get_nome(self):
        return self._nome

    def set_data_nascimento(self, data_nascimento):
        self._data_nasc = data_nascimento
    
    def get_data_nascimento(self):
        return self._data_nasc

    def set_altura(self, altura):
        self._data_altura = altura

    def get_altura(self):
        return self._altura  