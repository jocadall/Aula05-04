#5. Ler 10 números e imprimir quantos são pares e quantos são ímpares.
lista = [13, 16, 7, 21, 5, 8, 2, 25, 19, 10]
pares = 0
ímpares = 0
for n in lista:
    if n % 2 == 0:
        pares += 1
    else:
        ímpares += 1
print(f'\nDa lista {lista}: {pares} são pares e {ímpares} são ímpares.\n')
