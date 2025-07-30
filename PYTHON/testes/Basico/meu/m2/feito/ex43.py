p = float(input('Qual é o seu peso? '))
a = float(input('Qual é a sua altura? '))
IMC = p / (a * a)
if IMC < 18.5:
    print('Abaixo do peso')
elif IMC > 18.5 or IMC < 25:
    print('Peso ideal')
elif IMC > 25 or IMC < 30:
    print('Sobrepeso')
elif IMC > 30 or IMC < 40:
    print('Obesidade')
else:
    print('Obesidade morbida')