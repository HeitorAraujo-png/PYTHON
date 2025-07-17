y = int(input('Tabuada do: '))
for x in range(1, 11):
    print('{} * {:2} = {:2}'.format(y, x, (y * x)))