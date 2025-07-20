import pandas as pd
relatorio = pd.read_csv(r'PYTHON\teste.py\meu\ProjetoRelatorios\TESTEPD.csv', encoding='latin1')
cc = relatorio['C.C'] == 5000
dt = relatorio.DATA == '31/01/2025'
print(relatorio.any(dt and cc))