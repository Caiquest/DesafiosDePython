print('Hora da verdade, vamos calcular sua média:')
n1 = float(input('Digite sua primeira nota: '))
n2 = float(input('Digite sua segunda nota: '))
media = (n1 + n2) / 2
print(f'Tirando {n1} e {n2} sua média foi de {media:.1f}')
if media >= 7:
    print('Meus parabéns, você foi APROVADO!')
elif media >= 5 <= 6.9:
    print('OPS, você está de RECUPERAÇÃO!')
else:
    print('Infelizmente você foi REPROVADO!')