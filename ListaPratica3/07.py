# 7. Faça um programa que calcule e mostre a soma dos 50 primeiros números pares.
total = 0
q = 0
for i in range(1, 101):
    if i % 2 == 0 and i < 100:
        print(f'{i} + ', end='')
        total += i
        q += 1
    elif i % 2 == 0 and i == 100:
        total += i
        q += 1
        print(f'{i} = {total}')
print(f'Soma dos {q} primeiros números pares')
