num = int(input('Digite um número inteiro: '))
print(''' Escolha uma das bases para conversão: 
\033[0:31m[1] converter para BINÁRIO
[2] converter para OCTAL
[3] converter para HEXADECIMAL\033[m''')
opção = int(input('Sua opção: '))
if opção == 1:
    print('{} convertido para \033[0:35mBINÁRIO\033[m é igual a {}.'.format(num, bin(num)[2:]))
elif opção == 2:
    print('{} convertido para \033[0:31mOCTAL\033[m é igual a {}.'.format(num, oct(num)[2:]))
elif opção == 3:
    print('{} convertido para \033[0:33mHEXADECIMAL\033[m é igual a {}.'.format(num, hex(num)[2:]))
else:
    print('Opção inválida. Tente novamente.')


