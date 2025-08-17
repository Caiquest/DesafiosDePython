#sobrenome = input('Vamos verificar se seu nome possui o nome Silva, Digite seu nome completo: ')
#resposta = sobrenome.strip().lower().find('silva')
#print(f'VOCE POSSUI SILVA NO SOBRENOME ?{resposta!=-1}')
nome_completo = input('Digite seu nome completo e iremos verificar se possui Silva no seu nome: ')
tem_silva = 'silva' in nome_completo.lower().strip()
print(f'Voce possui "silva" no seu nome? {"Sim" if tem_silva else "Não"}')

