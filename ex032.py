from datetime import date
ano = int(input('Digite qualquer ano e te diremos se é um ano BISSEXTO OU NÃO, COLOQUE 0 PARA ANALISAR O ANO ATUAL: '))
if ano == 0:
    ano = date.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano %400 == 0:
    print(f'o ano {ano} é um ano bissexto')
else:
    print(f'{ano} não é um ano bissexto')