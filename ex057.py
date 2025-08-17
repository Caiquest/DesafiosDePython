#ler o sexo de uma pessoa com o while e só aceite respostas como "M" e "F" e caso esteja errado pedir a digitação novamente

while True:
    sexo = str(input('Digite seu sexo: [M/F]')).strip().upper()
    if sexo == "M" or sexo == "F":
        print(f"Você digitou o sexo {sexo}")
        break
    else:
        print("Sexo não aceito!")