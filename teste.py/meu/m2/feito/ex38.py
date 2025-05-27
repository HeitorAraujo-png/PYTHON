x = int(input('Digite um numero: '))
y = int(input('Digite outro numero: '))
if x > y:
    print('O primeiro numero ({}) é maior que o segundo ({})'.format(x, y))
elif x < y:
    print('O segundo numero ({}) é maito que o primeiro ({})'.format(y, x))
else:
    print('Os dois numero são iguais ({} e {})'.format(x, y))