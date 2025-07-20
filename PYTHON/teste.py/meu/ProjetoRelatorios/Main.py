import pandas as pd
relatorio = pd.read_csv(r'PYTHON\teste.py\meu\ProjetoRelatorios\TESTEPD.csv', encoding='latin1')
dt = relatorio[relatorio.DATA == '31/01/2025']
dtcc = dt[relatorio['C.C'] == 8115]
print(len(dtcc))