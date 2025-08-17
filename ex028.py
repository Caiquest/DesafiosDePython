from random import randint
from time import sleep
print('-=-' *20)
print('Vou pensar em um numero entre 0 e 5. Tente adivinhar...')
print('-=-' *20)
n = int(input('Em que número eu pensei?: '))
n1 = randint(0,5)
print('PROCESSANDO...')
sleep(2)
if n == n1:
    print('PARABÉNS voce acertou!!!')
else:
    print(f'HAHA EU GANHEI! o número que eu pensei foi o {n1} e não no {n}')
print('FIM!!!')