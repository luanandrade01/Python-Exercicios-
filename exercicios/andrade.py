nome = str(input('Qual é o seu nome completo? ')).strip()
print('Você tem \033[1;30mandrade\033[m no nome? \033[1;31m{}\033[m'.format('andrade' in nome.lower()))
