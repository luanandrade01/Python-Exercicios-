velocidade = float(input('Em que velocidade seu carro se encontra? '))
if velocidade > 80:
    print('\033[0;31mMULTADO! Você excedeu o limite permitido que é de 80km/h\033[m.')
    multa = (velocidade-80) * 7
    print('Você deve pagar de multa o valor de R$ {:.2f}.'.format(multa))
print('Digija com segurança!')