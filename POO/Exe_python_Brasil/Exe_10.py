'''Classe Bomba de Combustível: Faça um programa completo utilizando classes e métodos que:

    Possua uma classe chamada bombaCombustível, com no mínimo esses atributos:
    tipoCombustivel.
    valorLitro
    quantidadeCombustivel
    Possua no mínimo esses métodos:
    abastecerPorValor( ) método onde é informado o valor a ser abastecido
 e mostra a quantidade de litros que foi colocada no veículo
    abastecerPorLitro( ) método onde é informado a quantidade em litros de combustível 
e mostra o valor a ser pago pelo cliente.
    alterarValor( ) altera o valor do litro do combustível.
    alterarCombustivel( ) altera o tipo do combustível.
    alterarQuantidadeCombustivel( ) altera a quantidade de combustível restante na bomba.
    OBS: Sempre que acontecer um abastecimento 
é necessário atualizar a quantidade de combustível total na bomba.
'''
class Bomba_Combustivel:
    def __init__(self, tipo_combustivel : str, vlr_litro : float, qnt_combustivel : float):
        self.tipo_combustivel = tipo_combustivel
        self.vlr_litro = vlr_litro
        self.qnt_combustivel = qnt_combustivel
    
    def mostra_dados(self):
        print('--'*30)
        print('Bomba de combustível'.upper().center(60))
        print('--'*30)
        print('Tipo de combustível:', self.tipo_combustivel, '\nValor litro:', self.vlr_litro, 'R$',
'\nQuantidade de litros:', self.qnt_combustivel )
    
    def abastecer_Por_Valor(self):
        print('=-'*30)
        v = float(input('Digite o valor que deseja abastecer: '))
        l = v/self.vlr_litro
        self.qnt_combustivel -= l
        print(f'{l:.2f} litros')
    
    def abastecer_Por_Litro(self):
        print('=-'*30)
        l1 = float(input('Digite quantos litros deseja abastecer: '))
        self.qnt_combustivel -= l1
        l2 = (l1 * self.vlr_litro)
        print(f'{l2:.2f} R$')    
    
    def alterar_valor(self):
        print('=-'*30)
        nv_valor = float(input('Digite o novo valor: '))
        self.vlr_litro = nv_valor
    
    def alterar_combustível(self):
        print('=-'*30)
        nv_combus = str(input('Digite o novo combustível: '))
        self.tipo_combustivel = nv_combus
    
    def alterar_Quantidade_Combustivel(self):
        print('=-'*30)
        nv_qnt_combustivel = float(input('Quantidade de combustivel: '))
        self.qnt_combustivel = nv_qnt_combustivel
   
if __name__ == '__main__':
    
    bc = Bomba_Combustivel('álcool'.upper(), 6.02, 100)
    bc.mostra_dados()
    bc.abastecer_Por_Valor()
    bc.abastecer_Por_Litro()
    bc.alterar_valor()
    bc.alterar_combustível()
    bc.mostra_dados()
    bc.alterar_Quantidade_Combustivel()
    bc.mostra_dados()
    bc.abastecer_Por_Valor()
    bc.abastecer_Por_Litro()
    bc.mostra_dados()