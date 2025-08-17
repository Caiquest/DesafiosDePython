pr = float(input('Primeiro segmento: '))
seg = float(input('Segundo segmento: '))
ter = float(input('Terceiro segmento: '))
if pr < seg + ter and seg < pr + ter and ter < seg + pr:
    print('Os segmentos PODEM FORMAR um triângulo', end=' ')
    if pr == seg == ter:
        print('EQUILÁTERO')
    if pr != seg != ter != pr:
        print('ESCALENO')
    else:
        print('ISÓSCELES')
else:
    print('As retas NÃO PODEM formar um triângulo.')