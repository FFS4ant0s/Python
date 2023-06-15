"""
Classe Funcionário: Implemente a classe Funcionário.
Um empregado tem um nome (um string) e um salário(um double).
Escreva um construtor com dois parâmetros (nome e salário) e métodos para devolver nome e salário.
Escreva um pequeno programa que teste sua classe.
"""
class Funcionario:
    def __init__(self, nome : str, salario : float):
        self.nome = nome
        self.salario = salario

    def mostra_dados(self):
        print('--'*40)
        print(f'Nome: {self.nome}\nSalario: {self.salario}R$')
        print('--'*40)

    def aumenta_salario(self):
        aumento = float(input("Quantos % deseja aumentar ? "))
        valor_aumento = (self.salario * (aumento/100))
        self.salario += valor_aumento

if __name__ == '__main__':
    f = Funcionario('Fernando', 5000)
    f.mostra_dados()
    f.aumenta_salario()
    f.mostra_dados()