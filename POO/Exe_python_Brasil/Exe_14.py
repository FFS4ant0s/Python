"""
    Crie uma classe chamada BankAccount que tem os seguintes atributos e métodos:

    Atributos:

    num_conta (int): número da conta bancária (valor padrão é 0)
    saldo_conta (float): saldo da conta bancária (valor padrão é 0.0)
    taxa_juros (float): taxa de juros da conta bancária (valor padrão é 0.01)
    Métodos:

    deposito(amount: float) -> None: adiciona o valor amount ao saldo da conta.
    saque(amount: float) -> None: subtrai o valor amount do saldo da conta,
mas não permite que o saldo fique negativo.
    soma_juros() -> None: calcula e adiciona o juros ao saldo da conta.
    mostra_dados() -> None: exibe o número da conta e o saldo atual da conta.
    
    Além disso, crie uma classe derivada de BankAccount chamada SavingAccount
com um atributo adicional saldo_minimo (float) e sobrescreva o método saque()
para não permitir que o saldo da conta fique abaixo do saldo_minimo.

    Por fim, crie uma classe Customer que contém uma lista de contas bancárias
do cliente e os seguintes métodos:

    add_conta(account: BankAccount) -> None: adiciona uma conta bancária
à lista de contas do cliente.
    get_total_balanco() -> float: retorna o saldo total do cliente,
somando os saldos de todas as contas.
"""

class BankAccount:
    def __init__(self, num_conta : int = 0, saldo_conta : float = 0, taxa_juros : float = 0.01):
        self.num_conta = num_conta
        self.saldo_conta = saldo_conta
        self.taxa_juros = taxa_juros

    def deposito(self, amount):
        self.saldo_conta += amount

    def saque(self, amount):
        if self.saldo_conta - amount < 0:
            print("Saldo insuficiente.")
        else:
            self.saldo_conta -= amount

    def soma_juros(self):
        interest = self.saldo_conta * self.taxa_juros
        self.saldo_conta += interest

    def mostra_dados(self):
        print(f"Conta: {self.num_conta}, Saldo: {self.saldo_conta}")


class SavingAccount(BankAccount):
    def __init__(self, saldo_minimo : float = 0.0, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.saldo_minimo = saldo_minimo

    def saque(self, amount):
        if self.saldo_conta - amount < self.saldo_minimo:
            print("Não é possível sacar abaixo do saldo mínimo.")
        else:
            super().saque(amount)


class Customer:
    def __init__(self):
        self.accounts = []

    def add_conta(self, account):
        self.accounts.append(account)

    def get_total_balanco(self):
        return sum(account.saldo_conta for account in self.accounts)
    
if __name__ == '__main__':
    conta1 = BankAccount(num_conta = 1, saldo_conta = 1000.0, taxa_juros = 0.02)
    conta2 = SavingAccount(num_conta = 2, saldo_conta = 5000.0, taxa_juros = 0.03, saldo_minimo = 1000.0)
    conta3 = BankAccount(num_conta = 3)

    conta1.mostra_dados()
    conta2.mostra_dados()
    conta3.mostra_dados()
    conta1.deposito(500)
    conta2.deposito(500)
    conta3.deposito(500)
    conta1.mostra_dados()
    conta2.mostra_dados()
    conta3.mostra_dados()