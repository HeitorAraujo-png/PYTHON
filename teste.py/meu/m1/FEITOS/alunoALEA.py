import random
a1 = str(input('Digite o nome do(a) primeiro aluno(a): '))
a2 = str(input('Digite o nome do(a) segundo aluno(a): '))
a3 = str(input('Digite o nome do(a) terceiro aluno(a): '))
a4 = str(input('Digite o nome do(a) quarto aluno(a): '))
alunos = [a1, a2, a3 ,a4]
random.shuffle(alunos)
ale = random.choice(alunos)
print('O(A) aluno(a) sorteado(a) para limpar o quadro foi o(a) {}'.format(ale))
print('A ordem de apresentação vai ser {}'.format(alunos))
