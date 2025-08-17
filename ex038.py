a = int(input('Primeiro valor inteiro: '))
b = int(input('Segundo valor inteiro: '))
if a > b:
    print('O primeiro valor é maior.')
elif a < b:
    print(f'O segundo valor é maior.')
elif a == b:
    print('Os respectivos valores são iguais.')
else:
    print('Valor inválido')
