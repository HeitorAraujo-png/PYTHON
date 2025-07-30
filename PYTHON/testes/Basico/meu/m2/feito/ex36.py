casa = float(input('Qual é o valor da casa? '))
sala = float(input('Qual é o seu salario? '))
anos = int(input('Em quantos anos você quer parcelar a casa? '))
x = casa / (anos * 12)
y = sala * 0.3
if casa > x * y :
    print('Emprestimo negado')
else:
    print('Emprestimo Aprovado')