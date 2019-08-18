número = int(input('Digite um número qualquer: '))
resultado = número % 2
if resultado == 0:
    print('O número {} é PAR!'.format(número))
else:
    print('O número {} é ÍMPAR!'.format(número))