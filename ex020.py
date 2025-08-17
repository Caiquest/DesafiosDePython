from random import sample
n1 = input('Primeiro aluno: ')
n2 = input('Segundo aluno: ')
n3 = input('Terceiro aluno: ')
n4 = input('Quarto aluno: ')
todos = (n1, n2, n3, n4)
ordem = sample(todos, 4)
print (f'A ordem da lista será {ordem}')

