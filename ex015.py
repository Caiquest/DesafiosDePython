
km = float(input('Quantos km foram rodados com o carro ?: '))
dias = int(input('Quantos dias alugados?: '))
vd = dias * 60
kr = km * 0.15
total = kr + vd
print(f'O valor total a ser pago é de R${total:.2f}')