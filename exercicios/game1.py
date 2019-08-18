from random import randint
from time import sleep
itens = ('Pedra','Papel','Tesoura')
computador = randint(0,2)
print('''Suas opções:
[0] Pedra
[1] Papel 
[2] Tesoura''')
jogador = int(input('Qual é a sua jogada? '))
print('\033[0:31mPROCESSANDO...\033[m')
sleep(1)
print('='* 25)
print('Computador jogou {}'.format(itens[computador]))
print('Jogador jogou {}'.format(itens[jogador]))
print('='* 25)
if computador == 0: #Computador jogou Pedra.
    if jogador == 0:
        print('EMPATE!')
    elif jogador == 1:
        print('\033[0:34mVocê Venceu!')
    elif jogador == 2:
        print('\033[0:31mGAME-OVER')
    else:
        print('Jogada Inválida')
elif computador == 1: #Computador jogou Papel.
    if jogador == 0:
        print('\033[0:31mGAME-OVER!')
    elif jogador == 1:
        print('EMPATE!')
    elif jogador == 2:
        print('\033[0:34mVocê Venceu!')
    else:
        print('Jogada Inválida')
elif computador == 2: #Computador jogou Tesoura.
    if jogador == 0:
        print('\033[0:34mVocê Venceu!')
    elif jogador == 1:
        print('\033[0:31mGAME-OVER!')
    elif jogador == 2:
        print('EMPATE!')
    else:
        print('Jogada Inválida')
