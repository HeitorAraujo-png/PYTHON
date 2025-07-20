import pandas as pd

class Relatorios:
    
    def __init__(self):
        self.listaCC = [] 
        self.listaDIAS= []
        self.departamento = pd.read_csv(r'BACKEND_\CSV_ARQ\Dptdia.csv', encoding='latin1')
        self.relatorio = pd.read_csv(r'BACKEND_\CSV_ARQ\relatorio.csv', encoding='latin1')
        self.CentroCustos()
        self.Dias()
    
    def remove(self, lista):
        return list(dict.fromkeys(lista))
        
    def CentroCustos(self):
        for i in self.departamento.CC:
            self.listaCC.append(i)
        self.listaCC.sort()
        return self.remove(self.listaCC)
    
    def Dias(self):
        for i in self.departamento.DATA:
            self.listaDIAS.append(i)
        self.listaDIAS.sort()
        return self.remove(self.listaDIAS)
    
        
    def ok(self, cc, dia):
        dpdt = self.departamento[self.departamento['DATA'] == dia]
        dias = dpdt[dpdt.CC == cc]
        print(f'Centro de custo:{cc} | Quantia: {len(dias)} | Data: {dia}')
        
    def ln(self, dia):
        dt = self.departamento['29/01/2025'] == '29/01/2025'
        print(dt)
