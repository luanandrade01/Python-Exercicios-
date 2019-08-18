from random import randint
from time import sleep
computador = randint(0,5)
print('Vou pensar em um número entre 0 e 5. Tente adivinhar...')
jogador = int(input('Em que número eu pensei? '))
print('\033[0;31mPROCESSANDO...')
sleep(3)
if jogador == computador:
    print('\033[0;35mPARABÉNS! Você conseguiu me vencer!')
else:
    print('\033[0;31mVOCÊ PERDEU! Eu pensei no número {} e não no {}!'.format(computador,jogador))
