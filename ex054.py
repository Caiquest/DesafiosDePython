from datetime import date
anoatual = date.today().year
contmaior = 0
contmenor = 0
for c in range(1, 8):
    ano = int(input(f'Digite o {c}º ano de nascimento: '))
    if anoatual - ano >= 21:
        contmaior += 1
    else:
        contmenor += 1
print(f'O número de pessoas maiores de idade é de {contmaior} \nE o número de pessoas menores de idade é de {contmenor}')
