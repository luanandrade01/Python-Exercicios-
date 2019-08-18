preco = int(input('Digite o preço do produto: R$'))
novo  = preco - (preco*10/100)
print('O Preço do Produto que custava R${:.2f}, hoje com desconto de 5% custará R${:.2f}'.format(preco,novo))