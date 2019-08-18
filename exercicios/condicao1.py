tempo = int(input('Quantos anos tem seu carro? '))
if tempo<=3:
    print('\033[0;30mSeu carro é novinho\033[m!')
else:
    print('\033[1;31mSeu carro é velho\033[m!')