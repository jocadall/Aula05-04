#9. Faça um algoritmo que leia 10 números inteiros, armazene-os em uma lista e imprima em ordem crescente.
lista = []
while len(lista) < 10:
    try:
        n = int(input('\nNúmero: '))
        if n > 0:
            lista.append(n)
            lista.sort()
            print(lista)
    except ValueError:
        print("Entrada inválida. Digite um número inteiro positivo.")
        continue
print()
