#10. Dada a lista = [2, 4, 7, 2, 3, 3, 1, 0, 2, 6] imprima o número que se repete mais vezes.
lista = [2, 4, 7, 2, 3, 3, 1, 0, 2, 6]
quant = []
mais = 0
for n in lista:
    q = lista.count(n)
    quant.append(q)
    if q > mais:
        mais = n
print(f'{mais} é o número que se repete mais vezes. ')
