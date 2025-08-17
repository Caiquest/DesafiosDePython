from time import sleep
print('Carro passando pelo radar...')
print('Calculando média de velocidade...')
sleep(2)
velocidade = int(input('Qual a velocidade atual do carro? '))
v1 = (velocidade-80)*7
if velocidade <= 80:
    print('Velocidade dentro dos limites permitidos, dirija com segurança e tenha um bom dia !')
else:
    print(f'MULTADO, velocidade acima do permitido pela rodovia, voce será multado em R${v1:.2f} ')
