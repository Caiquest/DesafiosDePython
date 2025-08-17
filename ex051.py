print('==============OS 10 TERMOS DE UMA PA==============')
termo = int(input('Digite o primeiro termo: '))
razao = int(input('Digite a razão: '))
for c in range(0,10):
    pa = termo + razao * c
    print(f'{pa} →',end=" ")
print('FIM')