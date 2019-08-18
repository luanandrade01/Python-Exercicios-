from random import choice
nome1 = str(input('Primeiro Jogador:'))
nome2 = str(input('Segundo Jogador: '))
nome3 = str(input('Terceiro Jogador: '))
lista = [nome1,nome2,nome3]
escolhido = choice(lista)
print('O jogador escolhido foi {}.'.format(escolhido))
