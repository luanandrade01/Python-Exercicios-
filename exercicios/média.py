from math import ceil
from time import sleep
n1 = float(input('Primeira nota: '))
n2 = float(input('Segunda nota: '))
média = ceil(n1 + n2) / 2
print('\033[0:31mPROCESSANDO...\033[m')
sleep(2)
if média >= 7:
    print('Sua média foi {:.1f}, e você foi APROVADO! PARABÉNS!'.format(média))
elif média < 5:
    print('Sua média foi {:.1f}, e você foi REPROVADO! ESTUDE MAIS'.format(média))
else:
    print('Sua média foi {:.1f}, e você ficou em RECUPERAÇÃO!'.format(média))
