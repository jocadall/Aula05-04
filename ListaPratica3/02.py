#2. Fazer um programa para encontrar todos os números pares entre 1 e 100.
for n in range(1, 101):
    if n % 2 == 0:
        if n < 100:
            print(n, end=', ')
        else:
            print(n)
