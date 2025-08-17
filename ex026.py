frase = input('Digite uma frase: ').lower().strip()
letra = input('Digite uma letra da sua frase: ').lower().strip()
q = frase.count(letra)
p = frase.find(letra)+1
r = frase.rfind(letra)+1

print(f'A letra escolhida aparece {q} vezes na sua frase.')
print(f'A posição que ela aparece na primeira vez em sua frase foi {p}.')
print(f'A posição que ela aparece na ultima vez em sua frase foi {r}.')
