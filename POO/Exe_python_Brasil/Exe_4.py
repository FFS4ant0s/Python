'''Classe Pessoa: Crie uma classe que modele uma pessoa:

Atributos: nome, idade, peso e altura
Métodos: Envelhercer, engordar, emagrecer, crescer.
Obs: Por padrão, a cada ano que nossa pessoa envelhece, sendo a idade dela menor que 21 anos,
ela deve crescer 0,5 cm.'''

class Pessoa:
    def __init__(self, nome : str, idade : int, peso : float, altura : float):
        self.nome = nome
        self.idade = idade
        self.peso = peso
        self.altura = altura 

    def mostra_dados(self):
        
        print('Nome:', self.nome, '\nIdade:', self.idade,'anos', '\nPeso:', self.peso,'kg', '\nAltura:', self.altura/100, 'm')

    def envelhecer(self):
        envelhece = int(input('Quantos anos deseja envelhecer: '))
        ano = self.idade        
        for i in range(envelhece):
                ano += 1
                if ano < 21:
                      self.altura += 0.5                      
        
        nv_idade = self.idade + envelhece
        self.idade = nv_idade
                                                               
    def engordar(self):
            engorda = int(input('Quantos kg deseja engordar: '))
            nv_peso = self.peso + engorda
            self.peso = nv_peso                                               
                                          
    def emagrecer(self):
            emagrece = float(input('Quantos Kg deseja emagrecer: '))
            nv_peso = self.peso - emagrece
            self.peso = nv_peso            

    def crescer(self):
            cresce = float(input('Quantos cm deseja crescer: '))
            nv_altura = self.altura + cresce
            self.altura = nv_altura

if __name__ == '__main__':
    n = 'Nando'
    i = 30
    p = 50
    a = 200
    p1 = Pessoa(n, i, p, a)
    p1.mostra_dados()
    p1.envelhecer()
    p1.mostra_dados()
    p1.engordar()
    p1.mostra_dados()
    p1.emagrecer()
    p1.mostra_dados()
    p1.crescer()
    p1.mostra_dados()

