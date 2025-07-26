import hashlib as hl
senha = input('Teste para hash: ')
print(hl.sha256(senha.encode()).hexdigest())