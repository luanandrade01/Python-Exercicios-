n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
m = (n1 + n2)/2
print('Sua média é \033[0;33m{:.1f}\033[m'.format(m))
if m >= 7:
    print('\033[0;34mAPROVADO!. PARABÉNS!\033[m')
else:
    print('\033[0;31mREPROVADO!. ESTUDE MAIS\033[m!')
