from random import choice
primeiro = input('Primeiro aluno: ')
segundo = input('Segundo aluno: ')
terceiro = input('Terceiro aluno: ')
quarto = input('Quarto aluno: ')
sorte = (primeiro, segundo, terceiro, quarto)
sorte = choice(sorte)
print(f'O aluno sorteado foi {sorte}')