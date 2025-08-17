from random import choice
from time import sleep


print('=-'*20)
print('GAME PEDRA PAPEL OU TESOURA')
print('=-'*20)
print('CARREGANDO....')
sleep(1.5)

print('''BEM-VINDO AO JOGO
Escolha uma das opcões para jogar:
[ PEDRA ] 
[ PAPEL ] 
[ TESOURA ] 
''')
jogada = str(input('Qual a sua jogada?')).strip().upper()
if jogada != 'PEDRA' and jogada != 'PAPEL' and jogada != 'TESOURA':
    print('JOGADA INVÁLIDA, POR FAVOR TENTE NOVAMENTE.')
else:
    print('JO')
    sleep(1)
    print('KEN')
    sleep(1)
    print('POO!!!')
    sleep(1)
    computador = 'PEDRA',  'PAPEL', 'TESOURA'
    sort = choice(computador)
    print(f'A jogada do computador foi {sort}')
    print(f'A sua jogada foi {jogada}')
    if jogada == sort:
        print('Houve EMPATE!')

    if jogada == 'PEDRA' and sort == 'TESOURA':
        print('O jogador venceu!'.upper())
    elif jogada == 'PEDRA' and sort == 'PAPEL':
        print('O computador venceu!'.upper())

    if jogada == 'TESOURA' and sort == 'PEDRA':
        print('O computador venceu!'.upper())
    elif jogada == 'TESOURA' and sort == 'PAPEL':
        print('O jogador venceu!'.upper())

    if jogada == 'PAPEL' and sort == 'TESOURA':
        print('O computador venceu!')
    elif jogada == 'PAPEL' and sort == 'PEDRA':
        print('O jogador venceu!')




