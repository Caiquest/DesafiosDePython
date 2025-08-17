num = int(input('Digite um número inteiro: '))
base = int(input('Escolha uma base de conversão: \n[1]Binário \n[2]Octal \n[3]Hexadecimal\nSua Opção: '))
if base == 1:
    conversao = bin(num)[2:]
elif base == 2:
    conversao = oct(num)[2:]
elif base == 3:
    conversao = hex(num)[2:]
else:
    print('Número invalido, tente novamente.')
print(f'O número {num} convertido ficará como {conversao}.')