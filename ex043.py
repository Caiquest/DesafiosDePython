peso = float(input('Qual o seu peso? (Kg) '))
altura = float(input('Qual a sua altura? (m) '))
imc = peso / (altura ** 2)
print(f'O IMC dessa pessoa é de {imc:.1f}')
if imc < 18.5:
    print('A pessoa está abaixo do peso.')
elif imc <= 24.9:
    print('A pessoa está com o peso normal.')
elif imc <= 29.9:
    print('A pessoa está com sobrepeso.')
elif imc <=34.9:
    print('A pessoa está com obesidade grau 1.')
elif imc <= 39.9:
    print('A pessoa está com obesidade grau 2(severa).')
else:
    print('A pessoa está com obesidade grau 3(mórbida)')
