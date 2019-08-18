nomeCompleto = str(input('Digite seu nome completo: ')).strip()
print('Analisando seu nome...')
print('Seu nome completo em maíuscula é {}.'.format(nomeCompleto.upper()))
print('Seu nome completo em minuscula é {}.'.format(nomeCompleto.lower()))
print('Seu nome tem {} letras.'.format(len(nomeCompleto) - nomeCompleto.count(' ')))
print('Seu primeiro nome tem {} letras.'.format(nomeCompleto.find(' ')))


