import hashlib as hl
senha = input('Testo para hash: ')
senhahex = hl.sha256(senha.encode()).hexdigest()
print(senha)
print(senhahex, 'ok')