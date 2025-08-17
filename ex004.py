digito = input('Digite algo: ')
print(type(digito))
print(f'É um número ? {digito.isnumeric()}')
print(f'É alfabetico ? {digito.isalpha()}')
print(f'Contém letras ou números ? {digito.isalnum()}')
print(f'Está em letras maiusculas ? {digito.isupper()}')
print(f'Está em letras minusculas ? {digito.islower()}')
print(f'Está capitalizada ? {digito.istitle()}')



