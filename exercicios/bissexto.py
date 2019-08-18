from datetime import date
ano = int(input('Que ano você quer analisar? Coloque 0 para o ano atual: '))
if ano == 0:
    ano = date.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('O ano {} é \033[0;35mBISSEXTO\033[m!'.format(ano))
else:
    print('O ano {} NÂO É \033[0;31mBISSEXTO\033[m!'.format(ano))
