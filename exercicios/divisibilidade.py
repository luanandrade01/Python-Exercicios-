import math
número = int(input('Digite um número: '))
verificação = número % 2
if verificação == 0:
    print('{} é divisível por 2.'.format(número))
else:
    print('{} não é divisível por 2, pois não é um número par.'.format(número))