'''Classe Conta Corrente: Crie uma classe para implementar uma conta corrente.
A classe deve possuir os seguintes atributos: número da conta, nome do correntista e saldo.
Os métodos são os seguintes: alterarNome, depósito e saque;
No construtor, saldo é opcional, com valor default zero e os demais atributos são obrigatórios.'''

class Conta_Corrente:
    def __init__(self, num_conta : int, nome : str, saldo : float = 0):
        self.num_conta = num_conta
        self.nome = nome
        self.saldo = saldo

    def mostra_dados(self):
        print('--'*30)
        print('Nome:', self.nome, '\nNúmero da conta:', self.num_conta, '\nSaldo:', self.saldo )
        print('--'*30)

    def alterar_nome(self):
        nv_nome = str(input('Digite o nome: '))
        self.nome = nv_nome

    def depositar(self):
        deposito = float(input('Digite o valor a ser depósitado: '))
        nv_saldo = self.saldo + deposito
        self.saldo = nv_saldo

    def sacar(self):
        saque = float(input('Digite o valor que deseja sacar: '))
        if saque > self.saldo:
            print('--'*30)
            print('Saldo insuficiente para transação!!!'.upper())
        else:
            nv_saldo = self.saldo - saque
            self.saldo = nv_saldo

if __name__ == '__main__':
    c = Conta_Corrente(1111111, 'nando')
    c.mostra_dados()
    c.alterar_nome()
    c.mostra_dados()
    c.depositar()
    c.mostra_dados()
    c.sacar()
    c.mostra_dados()