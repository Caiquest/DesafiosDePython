from datetime import date
from time import sleep

print('ALISTAMENTO MILITAR')
print('carregando...')
sleep(1.5)
sexo = str(input('Digite o seu sexo : [M/F]\n')).strip().upper()[0]


data = date.today().year
if sexo == 'F':
    print('O ALISTAMENTO MILITAR É OBRIGATÓRIO SOMENTE PARA HOMENS !')
else:
    nascimento = int(input('Digite o ano de nascimento: '))
    idade = data - nascimento
    print(f'Quem nasceu em {nascimento} tem {idade} anos em {data}.')
    if idade == 17:
        print('Você está na idade de se alistar!')
    elif idade == 18:
        print('Você está na idade de se alistar!')
    elif idade <= 16:
        print(f'Você ainda não tem que se alistar, apenas daqui {17 - idade} anos em {17 - idade + data }')
    else:
        print(f'Você já passou da idade de se alistar e está atrasado em {idade - 17} anos, procure uma agência proxima e se aliste já!')

