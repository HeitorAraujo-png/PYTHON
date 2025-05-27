x = int(input('Digite um numero inteiro: '))
print('Em qual base de conversão você gostaria?\n- 1 para binario\n- 2 para octal\n- 3 para hexadecimal')
y = int(input('Digite sua opção: '))
if y == 1:
    print('{} para BINARIO é {}'.format(x, bin(x)[2:]))
elif y == 2:
    print('{} para OCTAL é {}'.format(x, oct(x)[2:]))
elif y == 3:
    print('{} para HEXADECIMAL é {}'.format(x, hex(x)[2:]))