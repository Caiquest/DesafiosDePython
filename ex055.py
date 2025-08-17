#lista = []
#   peso = float(input(f'Digite o peso da {c}º pessoa: '))
#    lista. append(peso)
#maior = max(lista)
# = min(lista)
#print(f'O maior peso foi de {maior:.2f} KG \nE o menor peso foi de {menor:.2f} KG')

maior = 0
menor = 0
for p in range (1, 6):
    peso = float(input(f'Digite o peso da {p}º pessoa: '))
    if p == 1:
        maior = peso
        menor = peso
    if peso > maior:
        maior = peso
    if peso < menor:
        menor = peso
print(f'O maior peso foi de {maior} KG e o menor peso foi de {menor} KG')
