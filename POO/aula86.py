# Método __call__
#  callable é algo que pode ser executado com parênteses
# Em classes normais, __call__ faz a instância de uma classe 'callable'

class CallMe:
    def __init__(self, phone):
        self.phone = phone
    
    def __call__(self, nome):
        print(nome, 'Chamando,' , self.phone)
        return 123

call1 = CallMe('619866115281')
retorno = call1('Nando')
print(retorno)