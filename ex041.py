from datetime import date

data = date.today().year
nascimento = int(input('Digite o ano de nascimento: '))
idade = data - nascimento
print(f'O atleta tem {idade} anos.')
if idade < 0 :
    print('ISTO É LOUCURA')
elif idade <= 9:
    print('O atleta deve ser inscrito na categoria MIRIM.')
elif idade <= 14:
    print('O atleta deve ser inscrito na categoria INFANTIL.')
elif idade <= 19:
    print('O aleta deve ser inscrito na categoria JUNIOR.')
elif idade <= 25:
    print('O atleta deve ser inscrito na categoria SÊNIOR.')
else:
    print('O atleta deve ser inscrito na categoria MASTER.')
