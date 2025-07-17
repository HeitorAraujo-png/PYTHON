r = ''
while 'm' != r  and 'f' != r:
    r = input('Digite seu sexo [M/F]: ').strip().lower()
    if 'm' != r and 'f' !=r:
        print('Tente novamente')
print('Fim')