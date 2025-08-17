'''
somaidade = 0
mediaidade = 0
homemvelho = 0
nomevelho = ''
mulher = 0

for p in range (1,5 ):
    print(f'--------{p}º pessoa--------')
    nome = str(input('Nome: ')).strip()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).strip()
    somaidade += idade
    if p == 1 and sexo in 'Mm':
        homemvelho = idade
        nomevelho = nome
    if sexo in 'Mm' and idade > homemvelho:
        homemvelho = idade
        nomevelho = nome
    if sexo in 'Ff' and idade < 20:
        mulher += 1

mediaidade = somaidade / 4
print(f'A média de idade é de {mediaidade} anos.')
print(f'O homem mais velho tem {homemvelho} anos e se chama {nomevelho}.')
print(f'O número de mulheres menores de 20 anos é de {mulher}.')
'''

homemvelho = 0
nomevelho = ''
somaidade = 0
mediaidade = 0
mulher = 0

for p in range (1, 5):
    print(f'----{p}º pessoa----')
    nome = str(input('Nome: ')).strip()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).strip()
    somaidade += idade
    if p == 1 and sexo in 'Mm':
        homemvelho = idade
        nomevelho = nome
    if sexo in 'Mm' and idade > homemvelho:
        homemvelho = idade
        nomevelho = nome
    if sexo in 'Ff' and idade < 20:
        mulher += 1

mediaidade = somaidade / 4
print(f'A média de idade é de {mediaidade} anos')
print(f'O homem mais velho tem {homemvelho} anos e se chama {nomevelho}')
print(f'Existem {mulher} mulheres menores de 20 anos.')