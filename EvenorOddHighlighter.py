print('\033[33m =============================== \033[30m')

print('\033[37m Digite um número e direi quais são pares ou ímpares. \033[30m')

print('\033[33m =============================== \033[30m')

print('\033[31m Vermelho = Ímpar \033[30m')
print('\033[32m Verde = Par \033[30m')

print('\033[33m =============================== \033[30m')


num = int(input('Digite um número: '))

for i in range(1, num + 1):

    if i %2 == 0:
        print(f'\033[32m {i}\033[30m ', end = ' ')

    else:
        print(f'\033[31m {i} \033[30m ', end = ' ')

