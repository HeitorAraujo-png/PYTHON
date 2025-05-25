c = input('Em que cidade você nasceu? ').strip().lower()
s = c.split()
if s[0] == 'santo':
    print('True')
elif s[0] == 'santos':
    print('True')
else:
    print('False')
    