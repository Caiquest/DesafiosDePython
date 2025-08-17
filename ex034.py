n = float(input('Qual o salário do funcionario ?'))
a = n+(n*10/100)
b = n+(n*15/100)
if n >= 1250:
    print(f'O salário do funcionario foi para RS{a:.2f}, pois teve um acrescimo de 10%')
else:
    print(f'O salario do funcionario foi para RS{b:.2f}, pois teve um acrescimo de 15%')