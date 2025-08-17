#Perguntar 4 vezes nome, idade e sexo, tirar média da idade, colocar o nome e idade do homem mais velho e quantas mulheres menores de 20 anos tem.
mediaidade = 0
nomevelho = ''
idadevelho = 0
mulher = 0
for p in range(1, 5):
    nome = str(input("Digite o nome: "))
    idade = int(input("Digite a idade: "))
    sexo = str(input("Sexo [M/F]: ")).upper()
    mediaidade += idade
    if sexo == "M" and idade > idadevelho:
        idadevelho = idade
        nomevelho = nome
    if sexo == "F" and idade < 20:
        mulher += 1
mediaidade /= 4
print(mediaidade)
print(idadevelho, nomevelho)
print(mulher)