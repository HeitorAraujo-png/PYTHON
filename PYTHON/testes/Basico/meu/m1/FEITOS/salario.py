s = float(input('Digite o seu salario: R$ '))
p = int(input('Quantos % você ira receber de aumento? '))
a = s*p/100
sa = s + a
print('Seu salario saiu de R${} para R${:.2f} com um aumento de {}%'.format(s, sa , p))