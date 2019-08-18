from datetime import date ##Biblioteca datetime.
atual = date.today().year ## Pegar o ano atual.
nasc = int(input('Ano de nascimento: ')) ## Entrada do ano de nascimento do usuário.
idade = atual - nasc # calculo o ano atual menos o ano que o usuário nasceu.
print('Quem nasceu em {} tem {} anos em {}.'.format(nasc, idade, atual))
if idade == 18:
    print('Você tem que se alistar IMEDIATAMENTE.')
elif idade < 18:
    saldo = 18 - idade
    print('Ainda faltam {} anos para o alistamento.'.format(saldo))
    ano = atual + saldo
    print('Seu alistamento será em {}.'.format(ano))
elif idade > 18:
    saldo = idade - 18
    print('Você já deveria ter se alistado há {} anos.'.format(saldo))
    ano = atual - saldo
    print('Seu alistamento foi em {}.'.format(ano))
