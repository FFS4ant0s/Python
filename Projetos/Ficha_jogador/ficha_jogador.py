def ficha(N='desconnhecido',G=0):
     N = input('Nome do jogador: ')
     G = input('Número de gols: ')
     if N == '':
          N = '<desconhecido>'
     if G == '':
          G = 0
     print('--'*30)
     print(f'O jogador {N} marcou {G} gols na  temporada .')

ficha()