import pandas as pd

class Relatorios:
    
    def __init__(self):
        self.departamento = pd.read_csv(r'CSV_ARQ\Dptdia.csv', encoding='latin1')
        df = self.departamento.copy()
        self.relatorio = df.groupby(['CC', 'DATA']).size().unstack(fill_value=0)
        self.conq = pd.read_csv(r'CSV_ARQ\relatorioConq.csv', encoding='latin1')
        self.relatorio.to_csv(r'CSV_ARQ\relatorio.csv', encoding='latin1')
        
    def Converte(self):
        self.relatorio = pd.concat(self.conq.values(), ignore_index=True)
        print(self.relatorio.head())
                
                
class RelatorioTeste:
    
    def __init__(self):
        self.listaCC = [] 
        self.listaDIAS= []
        self.departamento = pd.read_csv(r'CSV_ARQ\Dptdia.csv', encoding='latin1')
        self.relatorio = pd.read_csv(r'CSV_ARQ\relatorio.csv', encoding='latin1')
        self.CentroCustos()
        self.Dias()
        
    def remove(self, lista):
        return list(dict.fromkeys(lista))
        
    def Dias(self):
        for i in self.departamento.DATA:
            self.listaDIAS.append(i)
        self.listaDIAS.sort()
        return self.remove(self.listaDIAS)
    
    def CentroCustos(self):
        for i in self.departamento.CC:
            self.listaCC.append(i)
        self.listaCC.sort()
        return self.remove(self.listaCC)
        
    def ok(self, cc, dia):
        dpdt = self.departamento[self.departamento.DATA == dia]
        dias = dpdt[dpdt.CC == cc]
        print(f'Centro de custo:{cc} | Quantia: {len(dias)} | Data: {dia}')
        
    def ln(self, dia):
        dt = self.departamento['29/01/2025'] == '29/01/2025'
        print(dt)