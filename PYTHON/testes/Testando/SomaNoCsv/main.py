from services import *

csv = Geral(PathXlsx=r'arquivos\Relatorio.xlsx', PathCsv=r'arquivos\relatorio.csv')
csv.MakeArq()
csv.Tratamento()
csv.LGPD()