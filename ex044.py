print(f'{"LOJINHA CALANGOS":=^40}')


compra = float(input('Qual o valor das compras: R$'))
print('Qual a forma de pagamento?')
dinheiro = compra - (compra *0.10)
cartao = compra - (compra * 0.05)
tres = compra + (compra * 0.20)

pagar = int(input('[ 1 ] À vista no dinheiro/cheque \n[ 2 ] À vista no cartão \n[ 3 ] Em até 2x no cartão \n[ 4 ] 3x ou mais no cartão \nDigite a opção de pagamento: '))
if pagar == 1:
    print(f'Você escolheu pagar à vista no dinheiro, o valor da compra será de R$ {dinheiro:.2f}')
elif pagar == 2:
    print(f'Você escolheu pagar à vista no cartão, o valor da compra será de R$ {cartao:.2f}')
elif pagar == 3:
    np = int(input('Em quantas parcelas deseja pagar?'))
    if np <= 2:
        print(f'Você ira pagar R${compra:.2f} e parcelado no cartão ficará {2}x de R${compra/np:.2f}')
elif pagar == 4:
    np = int(input('Em quantas parcelas deseja pagar?'))
    if np >= 3 <= 12:
        print(f'Você ira pagar R${tres:.2f} em sua compra com 20% de juros, parcelado ficará {np}x de R${tres/np:.2f}')
