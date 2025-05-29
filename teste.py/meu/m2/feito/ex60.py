f = int(input('Digite um numero: '))
x = f
n = 1
while x > 0:    
    print('{}'.format(x),end=" " )
    print('X' if x > 1 else ' = ', end=" ")
    n *= x    
    x -= 1
print(n)