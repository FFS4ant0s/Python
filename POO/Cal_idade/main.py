from interface import Pessoa

def main():
    x = input('digite seu nome: ')
    y = input('Digite sua altura: ')
    z = input('Digite sua data de nascimento: ')
    
    pessoa = Pessoa(x, z, y)
    pessoa.imprimir_dados()
    print('-'*40)
    pessoa.calcular_idade()
    print('-'*40)

if __name__ == '__main__':
    main()