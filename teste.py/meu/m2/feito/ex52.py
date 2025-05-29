tot = 0
x = int(input('Digite um numero: '))
for i in range(1, x + 1):
    if x % i == 0:
        print('\033[31m\033[m', end=" ")
        tot += 1
        if tot == 2:
            print('Esse numero é primo')
        else:
            print('Esse numero não é primo')
    else:
        print('\033[34m\033[m', end=" ")
print('o {} foi divisivel {} vezes'.format(x, tot))