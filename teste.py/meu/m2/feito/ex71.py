v = 0
c = 50; cn = 0
t = 20; tn = 0
d = 10; dn = 0
u = 1; un = 0
while True:
    v = float(input('Digite o valor a ser sacado: '))
    while True:
        if v - c >= 0:
            v = v - c
            cn += 1
        else:
            break
    while True:
        if v - t >= 0:
            v = v - t
            tn += 1
        else:
            break
    while True:
        if v - d >= 0:
            v = v - d 
            dn += 1
        else:
            break
    while True:
        if v - u >= 0:
            v = v - u
            un += 1
        else:
            break
    break
print(f'''
    Total de {cn} cédulas de R$50
    Total de {tn} cédulas de R$20
    Total de {dn} cédulas de R$10
    Total de {un} cédulas de R$1
      ''')