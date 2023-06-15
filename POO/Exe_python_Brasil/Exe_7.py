"""
Classe Bichinho Virtual:Crie uma classe que modele um Tamagushi (Bichinho Eletrônico):

Atributos: Nome, Fome, Saúde e Idade 
b.Métodos: Alterar Nome, Fome, Saúde e Idade; Retornar Nome, Fome, Saúde e Idade 
Obs: Existe mais uma informação que devemos levar em consideração, o Humor do nosso tamagushi,
este humor é uma combinação entre os atributos Fome e Saúde, ou seja, um campo calculado,
então não devemos criar um atributo para armazenar esta informação por que ela pode ser calculada a qualquer momento.
"""

class Bichinho_virtual():
    def __init__(self, nome : str ,idade : int = 0 ,fome : float = 0 ,saude : float = 0):
        self.nome = nome
        self.fome = fome
        self.saude = saude
        self.idade = idade

    def mostra_dados(self):
        humor = (self.saude + self.fome)//2
        if humor >= 7:
            humor = 'Feliz'
        elif humor < 7 and humor >= 4:
            humor = 'Normal'
        else:
            humor = 'Triste'
        print('--'*30)
        print('Seu Bichinho Vitual'.center(60))
        print('--'*30)
        print('Nome:', self.nome, '\nIdade:', self.idade, '\nFome:', self.fome, '\nSaúde:', self.saude, '\nHumor:' ,humor)
        print('--'*30)

    def altera_nome(self):
        nv_nome = str(input('Digite o nome do seu bichinho: '))
        self.nome = nv_nome

    def altera_fome(self):
        while True:    
            nv_fome = float(input('Qual nível de fome do seu bichinho(0/10): '))
            if nv_fome < 0 or nv_fome > 10:
                print('--'*30)
                print('Digite um número de 0 a 10.')
                print('--'*30)
            else:
                self.fome = nv_fome
                break
        

    def altera_saude(self):
        while True:    
            nv_saude = float(input('Qual nível de saude do seu bichinho(0/10): '))
            if nv_saude < 0 or nv_saude > 10:
                print('--'*30)
                print('Digite um número de 0 a 10.')
                print('--'*30)
            else:
                self.saude = nv_saude
                break
        
    def altera_idade(self):
        nv_idade = int(input('Qual a idade do seu bichinho: '))
        self.idade = nv_idade

if __name__ == '__main__':
    bv = Bichinho_virtual('Tom',)
    bv.mostra_dados()
    bv.altera_nome()
    bv.mostra_dados()
    bv.altera_idade()
    bv.mostra_dados()
    bv.altera_saude()
    bv.mostra_dados()
    bv.altera_fome()
    bv.mostra_dados()
    