"""
Classe TV: Faça um programa que simule um televisor criando-o como um objeto.
O usuário deve ser capaz de informar o número do canal e aumentar ou diminuir o volume.
Certifique-se de que o número do canal e o nível do volume permanecem dentro de faixas válidas.
"""

class TV:
    def __init__(self, num_canal : int, volume : int):
        self.num_canal = num_canal
        self.volume = volume 

    def mostrar_dados(self):
        print('--'*30)
        print('Canal:', self.num_canal, '\nVolume:', self.volume)
        print('--'*30)
    
    def mudar_canal(self):
        while True:
            nv_canal = input('Digite o número do canal que deseja assistir(0/100): ')
            if nv_canal.isnumeric():
                nv_canal = int(nv_canal)
                if nv_canal >= 100 :
                    print('--'*30)
                    print('Não foi possível acha esse canal por favor tente novamente.')
                    print('--'*30)                   
                else:   
                    self.num_canal = nv_canal
                    break
            else:
                print('--'*30)
                print('Não foi possível acha esse canal por favor tente novamente.')
                print('--'*30)
    
    def decisão(self):
        while True:
            d = input('Deseja aumentar ou diminuir o volume(D/A)? ')
            print('--'*30)
            if d in 'DdAa':
                if d in 'Dd':
                    tv.diminui_volume(1)
                    break
                elif d in 'Aa':
                    tv.aumenta_volume(1)
                    break
            else:
                print('Por favor tente novamente.')
                print('--'*30)
        
    def aumenta_volume(self, x):
        nv_volume = self.volume + x
        self.volume = nv_volume
        
    def diminui_volume(self, y):
        nv_volume = self.volume - y
        self.volume = nv_volume

if __name__ == '__main__':
    tv = TV(10, 10)
    tv.mostrar_dados()
    tv.mudar_canal()
    tv.mostrar_dados()
    tv.decisão()
    tv.mostrar_dados()