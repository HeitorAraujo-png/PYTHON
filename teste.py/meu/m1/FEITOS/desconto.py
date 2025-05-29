p = float(input('Digite o preço do produto: '))
d = p*5/100
dp = p - d
print('Você tem 5% de desconto, e ganhara R${} de desconto \n O valor a ser pago é de R${}'.format(d, dp))