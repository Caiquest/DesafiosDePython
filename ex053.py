frase = str(input('Digite uma frase: ')).upper().strip()
palavras = frase.split()
junto = ''.join(palavras)
inverso = junto[::-1]
print(f'o inverso de {junto} é {inverso}')
if inverso == junto:
    print('É um palíndromo!')
else:
    print('Não é um palíndromo!')

