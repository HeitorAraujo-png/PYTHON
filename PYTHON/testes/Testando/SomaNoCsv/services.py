import pandas as pd
from openpyxl import load_workbook
# cd PYTHON\testes\Testando\SomaNoCsv
class SomandoTotal:
    
    def __init__(self):
        path = 'Pasta1.csv'
        csv = pd.read_csv(path, encoding='utf-8')
        csv.to_csv(path, index=True, encoding='utf-8')
        lis = []
        for i in range(1, 6):
            num = f'=SUM(A{2 + i - 1}:D{2 + i - 1})'
            lis.append(num)
        csv['tbl5'] = lis
        csv.to_csv(path, index=True)
        csv.replace('@', '')
        csv.to_excel('Pasta1.xlsx', index=False)
