c = 1
while c != 10:
    p = int(input('Digite o primeiro termo: '))
    r = int(input('Digite a razão: '))
    while c != 10:
        x = p + (c - 1) * r
        print(x)
        c += 1
    