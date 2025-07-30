s = 's'
c = 1
while s == 's':
    p = int(input('Digite o termo: '))
    r = int(input('Digite a razão: '))
    while c < 11:
        x = p + (c - 1) * r
        print(x)
        c += 1
    t = int(input('Deseja mostrar mais quantos termos? '))
    if t >= 1:
        t += c
        while c != t:
            x = p + (c -1) * r
            print(x)
            c += 1
    s = input('Deseja continuar [S/N]? ').strip().lower()