"""
    Classe Conta de Investimento: 
    
    Faça uma classe contaInvestimento que seja semelhante a classe contaBancaria,
com a diferença de que se adicione um atributo taxaJuros.
    Forneça um construtor que configure tanto o saldo inicial como a taxa de juros. 
    Forneça um método adicioneJuros (sem parâmetro explícito) que adicione juros à conta.
    Escreva um programa que construa uma poupança com um saldo inicial de R$1000,00 e uma taxa de juros de 10%.
    Depois aplique o método adicioneJuros() cinco vezes e imprime o saldo resultante.
"""

class Conta_Investimento:
    def __init__(self, saldo : float = 2000000, tx_juros : float = 6.17 ):
        self.saldo = saldo
        self.tx_juros = tx_juros

    def mostra_dados(self):
        print('--'*30)
        
        print(f'Saldo: {self.saldo:.2f} R$ \nTaxa de Juros: {self.tx_juros} %')
    
    def adicionajuros(self):
        juros = self.tx_juros/100
        vj = self.saldo * juros
        self.saldo += vj

if __name__ == '__main__':
        ci = Conta_Investimento()
        ci.mostra_dados()
        ci.adicionajuros()
        ci.mostra_dados()
        ci.adicionajuros()
        ci.mostra_dados()
        ci.adicionajuros()
        ci.mostra_dados()
        ci.adicionajuros()
        ci.mostra_dados()