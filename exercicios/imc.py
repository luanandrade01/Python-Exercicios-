peso = float(input('Qual é o seu peso: (Kg)'))
altura = float(input('Qual é a sua altura: (m)'))
imc = peso / (altura ** 2)
print('O IMC dessa pessoa é de {:.1f}'.format(imc))
if imc < 18.5:
    print('ABAIXO DO PESO NORMAL.')
elif 18.5 <= imc < 25:
    print('PESO IDEAL.')
elif 25 <= imc < 30:
    print('SOBREPESO.')
elif 30 <= imc < 40:
    print('OBESIDADE.')
elif imc >= 40:
    print('OBESIDADE MÓRBIDA.')
