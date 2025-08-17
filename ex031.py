n1 = int(input('Qual a distancia da sua viagem? '))
print(f'Sua viagem será de {n1}KM, o valor do transporte será de 0.50 centavos para viagens de até 200KM com DESCONTO com valor de 0.45 centavos para viagens acima de 200KM! ')
if n1 <= 200:
    print(f'o valor da sua viagem será de R${n1*0.50:.2f}')
else:
    print(f'O valor da sua viagem será de R${n1*0.45:.2f}')