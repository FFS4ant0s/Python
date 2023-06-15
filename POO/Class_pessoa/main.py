from Cod import Pessoa

def main():
    pessoa = Pessoa('Fernando', '05/02/2000', 1.77)
    pessoa.imprimi_dados()
    pessoa.cal_idade()

if __name__ == '__main__':
    main()   