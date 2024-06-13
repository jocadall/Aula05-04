#3. Ler um valor inteiro (aceitar somente valores entre 1 e 10) e escrever a tabuada de 1 a 10 do valor lido.
while True:
    n = int(input('\nTabuada de 1 a 10\nDigite um valor inteiro de 1 a 10: '))
    if n > 0 and n < 11:
        for i in range(1, 11):
            print(f'{n} x {i} = {n*i}')
    else:
        print('Valor inválido!!! ')
        continue
