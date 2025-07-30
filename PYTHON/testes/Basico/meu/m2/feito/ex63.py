n = int(input('Digite um numero para a sequencia de fibonnaci: '))
n1 = 0
n2 = 1
c = 1
while c < n:
    n3 = n2 + n1
    print(n1,'>',n2 ,'>',n3 , end=" > ")
    n1 = n2 + n3
    n2 = n1 + n3
    c += 1
print('Fim')

