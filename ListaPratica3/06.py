#6. Utilizando a estrutura de repetição for, faça um programa que receba 10 números e conte quantos deles estão no intervalo [10,20] e quantos deles estão fora do intervalo.
lista = []
for i in range(10):
    n = int(input('\nNúmero: '))
    lista.append(n)
dentro = 0
fora = 0
for item in lista:
    if item >= 10 and item <= 20:
        dentro += 1
    else:
        fora += 1
print(f'\nDesses números {dentro} deles estão no intervalo [10,20] e {fora} deles estão fora do intervalo.\n')
