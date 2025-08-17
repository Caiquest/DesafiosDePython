nome = input('Digite seu nome completo: ').lower().strip()
primeiro_nome = nome.split()
print(f'Muito prazer em te conhecer {nome}')
print(f'Seu primeiro some é {primeiro_nome[0]} e o ultimo nome {primeiro_nome[-1]}')