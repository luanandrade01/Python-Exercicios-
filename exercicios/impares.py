soma = 0
cont = 0
for c in range(1,501,2):
    if c % 3 == 0:
        soma = soma + c #acumulador soma todos os números ímpares.
        cont = cont + 1 #conta todos números.
print('A soma de todos os {} valores solicitados é {}.'.format(cont,soma))


