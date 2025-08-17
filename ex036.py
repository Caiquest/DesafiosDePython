print('=-'*20)
print('SIMULAÇÃO DE EMPRÉSTIMO')
print('=-'*20)
casa = float(input('Qual o valor da casa? R$ '))
salario = float(input('Informe qual o seu salário: R$ '))
anos = int(input('Em quantos anos pretende pagar ? '))
valor = casa / (anos * 12)
if valor < salario * 0.3:
    print(f'O valor da prestação ficará de R${valor:.2f} e terá que pagar em {anos} anos, EMPRÉSTIMO APROVADO, PARABÉNS!.')
else:
    print(f'O valor da prestação ultrapassa 30% do salario do senhor(a), o valor das parcelas ficariam em R${valor:.2f}, EMPRÉSTIMO NEGADO.')


