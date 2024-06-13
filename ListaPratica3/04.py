#4. Leia várias idades e calcule a média entre as idades (usar uma variável para idade).
ages = [19, 21, 25, 30]
for age in ages:
    print(f'{age} anos de idade. ')

print(f'A média entre essas idades é {sum(ages)/len(ages)}')
