print('=-'*20)
print('Analisador de Triangulos')
print('=-'*20)
pr = float(input('Primeiro segmento: ').strip())
seg = float(input('Segundo segmento: ').strip())
ter = float(input('Terceiro segmento: ').strip())
if pr + seg > ter and pr + ter > seg and seg + ter > pr:
    decisao = 'PODEM'
else:
    decisao = 'NÃO PODEM'
print(f'As retas {decisao} formar um triangulo')
