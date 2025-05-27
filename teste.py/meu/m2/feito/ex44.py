v = float(input('Qual é o valor a ser pago? '))
pg = str(input('Forma de pagamento: ')).strip().lower()
if 'cartão' in pg or 'cartao' in pg or 'debito' in pg or 'credito' in pg:
    x = int(input('Em quantas vezes você quer parcelar? '))
    if x == 2:
        print('O valor a ser pago é de R${}'.format(v))
    elif x == 1:
        print('O valor a ser pago é de R${}'.format(v - (v * 0.05)))
    else:
        print('O valor a ser pago é de R${}'.format(v + (v * 0.20)))
elif 'dinheiro' in pg or 'cheque' in pg:
    print('O valor a ser pago é de R${}'.format(v - (v * 0.10)))