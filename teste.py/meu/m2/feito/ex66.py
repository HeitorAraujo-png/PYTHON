c = s = 0
while True:
    n = int(input('Digite um numeros (999 para parar): '))
    if n == 999:
        break
    s += n
    c += 1
print(f'Foram digitados um total de {c} numero e a soma de tudo foi de {s}')