
n1 =  int(input('Digite um numero: '))
n2 =  int(input('Digite outro numero: '))
n3 =  int(input('Digite mais um numero: '))
l = [n1, n2, n3]
l.sort(reverse=True)
print('A sequencia decresente é {}, {}, {},'.format(l[0], l[1], l[2]))
"""

n1 =  int(input('Digite um numero: '))
n2 =  int(input('Digite outro numero: '))
n3 =  int(input('Digite mais um numero: '))
menor = n1
if n2<n1 and n2<n3:
    menor = n2
if n3<n1 and n3<n2:
    menor = n3
print('O menor numero é {}'.format(menor))
maior = n1
if n2>n1 and n2>n3:
    maior = n2
if n3>n1 and n3>n2:
    maior = n3
print('O maior digito é: {}'.format(maior))
"""