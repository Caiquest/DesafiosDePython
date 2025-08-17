#jogo de advinhacao, computador pensa um numero de 0 a 10 e o usuario tem que adivinhar ate acertar, no fim mostrar a quantidade de tentativas

contador = 0
from random import randint
while True:
    num = int(input('Adivinhe um número de 0 a 10: '))
    jogada = randint(0,10)
    contador += 1
    if num == jogada:
        print(f'O número escolhido foi {jogada} e você acertou, Parabéns')
        break
    else:
        print(f'Que pena a jogada do computador foi {jogada}, você errou ! TENTE NOVAMENTE.')
print(f'Você tentou {contador} vezes.')