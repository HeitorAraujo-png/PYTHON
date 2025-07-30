t = 0
while True:
    t = int(input('Digite um numero: '))
    if t < 0:
        break
    for i in range(1, 10):
        print(f'{t} * {i} = {t * i}')
print('Fim')