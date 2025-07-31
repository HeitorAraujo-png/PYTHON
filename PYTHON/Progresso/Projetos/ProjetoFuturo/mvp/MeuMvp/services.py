import pandas as pd
from openpyxl import *
from django.conf import settings
import os

# * cd PYTHON\testes\Testando\SomaNoCsv
 
# ! = IMPORTANTE
# ? = OQUE FAZ
# TODO = A FAZER
# * = AVISOS


# class Relatorios:
    
#     def __init__(self, files):
#         self.fileG = self.fileF = pd.read_csv(files)
    
#     def Separa(self):
#         Geral = 'RelatorioGeral.xlsx'
#         Financeiro = 'RelatorioFinanceiro.xlsx'
#         self.fileG.to_excel(os.path.join(settings.MEDIA_ROOT, Geral), index=False)
#         self.fileF.to_excel(os.path.join(settings.MEDIA_ROOT, Financeiro), index=False)
#         return Geral, Financeiro


class Geral:
    
    def __init__(self, PathXlsx, nome):
        self.Path = PathXlsx
        self.nome = nome
        
    def MakeArq(self):
        if self.Path.endswith('.xlsx'):
            self.csv = pd.read_excel(self.Path)
            self.csv.to_csv(os.path.join(settings.MEDIA_ROOT, 'Arq.csv'), index=True, encoding='utf-8', sep=';')
        elif self.Path.endswith('.csv'):
            self.csv = pd.read_csv(self.Path, sep=';')
            self.csv.to_csv(os.path.join(settings.MEDIA_ROOT, 'Arq.csv'), index=True, encoding='utf-8', sep=';')
        else: return 'erro'
        
    def Tratamento(self):
        lista = {}
        self.Geral = pd.DataFrame()
        for i, rows in self.csv.iterrows():
            lista['cod'] = rows['cod']
            lista['nome'] = rows['nome']
            lista['cpf'] = rows['cpf']
            self.Geral = pd.concat([self.Geral, pd.DataFrame([lista])], ignore_index=False)
        self.Geral.to_excel(os.path.join(settings.MEDIA_ROOT, 'DeuCerto.xlsx'), index=False)
        return 'DeuCerto.xlsx'
            
    def LGPD(self):
        conteudo = os.listdir('arquivos/')
        arquivos = [item for item in conteudo if os.path.isfile(os.path.join(settings.MEDIA_URL, item))]
        for i in arquivos:
            os.remove(f'{os.path.join(settings.MEDIA_URL, i)}')
            
            
        
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