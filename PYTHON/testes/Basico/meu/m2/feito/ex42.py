a = float(input('Digite o primeiro segmento: '))
b = float(input('Digite o segundo segmento: '))
c = float(input('Digite o terceiro segmento: '))    
if a < b + c and b < a + c and c < a + b:
    print('Pode ser um triangulo')
    if a == b == c:
        print('Triangulo equilatero')
    elif a == b or a == c or b == c or b == a or c == a or c == b:
        print('Triangulo isosceles')
    else:
        print('Triangulo escaleno')
else:
    print('Não pode ser um triangulo')
