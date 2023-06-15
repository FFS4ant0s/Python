'''
Soma dos valores dos produtos!!
'''
def lin():
    print('-'*42)

def cabeca(txt):
    lin()
    print(txt)
    lin()

cabeca('Mercadinho do nando'.center(42))

car = []
cont = 0
while True:
    y = str(input('Produto: '))
    lin()
    
    if not y.isalpha():
        print('Não foi possível cadastrar o produto por favor tente novamente.')
        lin()
        continue 
    
    try :
        x = float(input('Digite o preço do produto: '))
        lin()
        
    except ValueError:
        lin()
        print('Não foi possível cadastrar o preço por favor tente novamente.')
        lin()
        continue
    
    car.append(x)
    
    c = input('Deseja continuar(Ss/Nn)? ')
    if c in 'Ss':               
        lin()
        cont += 1
        continue           

    elif c in 'Nn':
        lin()
        p = sum(car)
        print(f'o preço a ser pago será {p}R$.')    
        lin()
        print('Volte sempre.')        
        break
    
    else:
        lin()
        print('Não entendi.')
        lin()
        
        while c not in 'SsNn':
            c = input('Deseja continuar(Ss/Nn)? ')
            lin()
                    
    

    
