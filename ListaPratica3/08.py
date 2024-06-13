#8. Faça um algoritmo que leia um número positivo e imprima seus divisores.
while True:
    try:
        lista = []
        n = int(input('\nNúmero: '))
        if n > 0:
            for div in range(1, n + 1):
                if n % div == 0:
                    lista.append(div)
            print(f'D({n}) = {lista}')
            if len(lista) == 2:
                print(f'{n} é um número primo!! ')
        else:
            print("Entrada inválida. Digite um número inteiro positivo.")
    except ValueError:
        print("Entrada inválida. Digite um número inteiro positivo.")
