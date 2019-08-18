dias = int(input('Quantos dias o carro alugado? '))
km = float(input('Quantos km rodado? '))
pago = (dias * 60) + (km * 0.15)
print('O total à pagar é R${:.2f}'.format(pago))
