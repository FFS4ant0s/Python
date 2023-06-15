from datetime import datetime

class Pessoa:

    def __init__(self, nome, data_nasc, altura):
        self._nome = nome
        self._data_nasc = data_nasc
        self._altura = altura
 
    # método que define o nome da pessoa
    def set_nome(self, nome):
        self._nome = nome
    
    # método que obtém o nome da pessoa
    def get_nome(self):
        return self._nome
    
    # método que define a data de nascimento da pessoa
    def set_data_nascimento(self, data_nasc):
        self._data_nasc = data_nasc
    
    # método que obtém a data de nascimento da pessoa
    def get_data_nascimento(self):
        return self._data_nasc
    
    # método que define a altura da pessoa
    def set_altura(self, altura):
        self._data_altura = altura
    
    # método que obtém a altura da pessoa
    def get_altura(self):
        return self._altura 
    
    def imprimir_dados(self):
        print('Nome:', self._nome, '\nData de Nascimento:' ,
            self._data_nasc, '\nAltura:', self._altura)

    # método que calcula a idade da pessoa
    def calcular_idade(self):
    # vamos obter o ano da data de hoje
        ano_data_atual = datetime.today().year
    # agora vamos obter o ano de nascimento da pessoa
        partes_data_nascimento = self._data_nasc.split("/")
        ano_nascimento = partes_data_nascimento[2]
    # agora mostramos a idade da pessoa
        anos = ano_data_atual - int(ano_nascimento)
        print(self._nome, 'tem', anos, "anos.")
