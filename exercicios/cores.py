nome = str(input('Digite seu nome: ')).strip()
print('Seu nome é \033[0;32m{}\033[m.'.format(nome))

idade = int(input('Digite sua idade: '))
print('Sua idade é \033[0;31m{}\033[m.'.format(idade))
