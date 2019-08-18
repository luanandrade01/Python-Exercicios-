print('Analisador de Triangulos')
r1 = float(input('Primeiro Segmento: '))
r2 = float(input('Segundo Segmento: '))
r3 = float(input('Terceiro Segmento: '))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Os segmentos acima PODEM FORMAR TRIANGULOS,', end='')
    if r1 == r2 == r3:
        print('EQUILÁTERO!') # TODOS OS LADOS IGUAIS
    elif r1 != r2 != r3 != r1:
        print('ESCALENO!') # TODOS OS LADOS DIFERENTES
    else:
        print('ISÓSCELES!') # DOIS LADOS IGUAIS
else:
    print('Os segmentos acima NÃO PODEM FORMAR TRIANGULOS!')
