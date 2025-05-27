# from math import factorial; x = int(input('Digite um numero: ')); print(factorial(x))
r = int(input('Digite um numero: '))
t = r - 1
l = []
while t != 1:
    z = r * t
    r = z
    l.append(r)
    t -= 1
print(l)
