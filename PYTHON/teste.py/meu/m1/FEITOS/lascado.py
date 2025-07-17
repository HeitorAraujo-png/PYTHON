c = input('Em que cidade você nasceu? ').strip().lower()
s = c.split()
if 'santo' in s:
    print('True')
elif 'santos' in s:
    print('True')
else:
    print('False')
    