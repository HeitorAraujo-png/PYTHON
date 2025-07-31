import hashlib as hl; i = 0; li = []
while True:
    senha = input('Teste para hash: ')
    li.append(hl.sha256(senha.encode()).hexdigest())
    
    if i == 10:
        break
    i += 1
print(f'{'\n'.join(li)}')