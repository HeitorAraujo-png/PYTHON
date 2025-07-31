import pandas as pd
from openpyxl import load_workbook
import os
# * cd PYTHON\testes\Testando\SomaNoCsv
 
# ! = IMPORTANTE
# ? = OQUE FAZ
# TODO = A FAZER
# * = AVISOS

class Geral:
    
    def __init__(self, PathXlsx, PathCsv):
        self.PathCsv = PathCsv
        self.PathXlsx = PathXlsx
        
    def MakeArq(self):
        if self.PathXlsx.endswith('.xlsx'):
            xlsx = pd.read_excel(self.PathXlsx)
        elif self.PathXlsx.endswith('.csv'):
            xlsx = pd.read_csv(self.PathXlsx, sep=';')
        xlsx.to_csv(self.PathCsv, encoding='utf-8',sep=';' , index=False)
        self.csv = pd.read_csv(self.PathCsv, encoding='utf-8', sep=';')
        self.csv.to_csv(self.PathCsv, index=True, encoding='utf-8', sep=';')
        
    def Tratamento(self):
        lista = {}
        Geral = pd.DataFrame()
        for i, rows in self.csv.iterrows():
            lista['cod'] = rows['cod']
            lista['nome'] = rows['nome']
            lista['cpf'] = rows['cpf']
            Geral = pd.concat([Geral, pd.DataFrame([lista])], ignore_index=True)
            print(lista)
        Geral.to_csv('DeuCerto.csv')
            
    def LGPD(self):
        conteudo = os.listdir('arquivos/')
        arquivos = [item for item in conteudo if os.path.isfile(os.path.join('arquivos/', item))]
        for i in arquivos:
            os.remove(f'arquivos/{i}')
            
            
        
    # ? Pega index de coluna especifica
    # ? Exemplo: print(self.csv.columns.to_list()) vai voltar uma lista com todas as colunas do arquivo
    # ? ['cod', 'nome', 'cpf', 'telefone', 'cc', 'valor', 'local']
    # ? Vamos dizer que search = 'cc'
    # ? index = self.csv.columns.to_list().index(search)
    # ? print(index) >>> vai retornar 4
    # ? return alfabeto[index] >>> vai retornar 'e'
    def TakeIndex(self, search):
        alfabeto = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
        index = self.csv.columns.to_list().index(search)
        return alfabeto[index]





class Financeiro(Geral):

    def __init__(self, xlsx, csv):
        super().__init__(PathCsv= csv, PathXlsx= xlsx)
    
    def CentroCustos(self):
        centro = self.Limpa()
        lista = []
        for i in range(0, len(centro)):
            cut = str(centro[i])
            intercompany = f'{cut[0]}{cut[1]}'
            CentroCusto = f'{cut[2]}{cut[3]}'
            if intercompany == '81':
                emp = 'TVCA'
            if intercompany == '65':
                emp = 'Portal MT'
            if intercompany == '69':
                emp = 'FMCA'
            if intercompany == '85':
                emp = 'On Line(MT)'
            if CentroCusto == '03':
                area = 'ADM'
            if CentroCusto == '06':
                area = 'RH'
            if CentroCusto == '10':
                area = 'COMERCIA'
            if CentroCusto == '11':
                area = 'OPEC'
            if CentroCusto == '12':
                area = 'MKT'
            if CentroCusto == '14':
                area = 'PROGRAMAÇÃO'
            if CentroCusto == '15':
                area = 'JORNALISMO'
            if CentroCusto == '21':
                area = 'TECNOLOGIA'
            # TODO ADICIONAR AREA DA DIRETORIA !
        lista.append(f'{centro[i]} - {area} - {emp}')
        return lista


    def Limpa(self, lista):
        return list(dict.fromkeys(sorted(lista)))
    
    def Centros(self):
        lista = self.Limpa(self.csv.cc.to_list())
        print(lista)



    # ? Função para soma
    
    # ? def Sum(self):
    # ?     lis = []
    # ?     for i in range(1, 6):
    # ?         num = f'=SUM(A{2 + i - 1}:D{2 + i - 1})'
    # ?         lis.append(num)
    # ?     self.csv['tbl5'] = lis
    # ?     self.csv.to_csv(self.pathCSV, index=True)
    # ?     self.csv.to_excel('arquivos/Pasta1.xlsx', index=False)