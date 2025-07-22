import pandas as pd

class Relatorios:
    
    def __init__(self):
        self.departamento = pd.read_csv(r'CSV_ARQ\Dptdia.csv', encoding='latin1')
        self.Add()
        self.relatorio = pd.read_csv(r'CSV_ARQ\relatorio.csv', encoding='latin1')
        

            
    def remove(self, lista):
        lista.sort()
        return list(dict.fromkeys(lista))
        
    def Dias(self):
        lista = []
        for i in self.departamento.DATA:
            lista.append(i)
        return self.remove(lista)
        
    def CentroCustos(self):
        lista = []
        for i in self.departamento.CC:
            lista.append(i)
        return self.remove(lista)
        
    def Converte(self):
        centros = self.CentroCustos()
        dias = self.Dias()
        for cc in centros:
            nova_linha = {'DPT': cc}
            soma = 0
            for dia in dias:
                qtd = len(self.departamento[(self.departamento['CC'] == cc) & (self.departamento['DATA'] == dia)])
                nova_linha[dia] = qtd
                soma += qtd
            
            nova_linha['Total'] = soma
            nova_linha['Valor total'] = f'R$ {soma * 20:.2f}'
            
            
            self.relatorio = pd.concat([self.relatorio, pd.DataFrame([nova_linha])], ignore_index=True)
        for dia in dias:
            linha = {dia: 0}
            soma = 0
            for cc in centros:
                qtd = len(self.departamento[(self.departamento['C.C'] == cc) & (self.departamento['DATA'] == dia)])
                soma += qtd
            linha[dia] = soma
            self.relatorio = pd.concat([self.relatorio, pd.DataFrame([linha])], ignore_index=True)

        self.relatorio.to_csv(r'CSV_ARQ\relatorio_atualizado.csv', index=False, encoding='latin1')
        # self.relatorio.to_excel(r"EXCEL_ARQ\relatorio_atualizado.xlsx", index=False)
                
                
class RelatorioTeste:
    
    def __init__(self):
        self.departamento = pd.read_csv(r'CSV_ARQ\Dptdia.csv', encoding='latin1')
        self.dias = self.Dias()
        self.Add()
        self.centros = self.CentroCustos()
        self.relatorio = pd.read_csv(r'CSV_ARQ\relatorio.csv', encoding='latin1')
        
    def Add(self):
        with open(r'CSV_ARQ\relatorio.csv', 'r', encoding='latin1') as arq:
            arq = (arq.readlines())
            with open(r'CSV_ARQ\relatorio.csv', 'w', encoding='latin1') as csv:
                for i in arq:
                    csv.write(f'{i[:i.find(',') + 1]}{','.join(self.dias)},{i[i.find('Total'):]}')

    def remove(self, lista):
        return list(dict.fromkeys(sorted(lista)))

    def Dias(self):
        return self.remove(list(self.departamento.DATA))

    def CentroCustos(self):
        return self.remove(list(self.departamento['C.C']))

    def money(self):
        money = 0
        for cc in self.centros:
            soma = 0
            for dia in self.dias:
                qtd = len(self.departamento[(self.departamento['C.C'] == cc) & (self.departamento['DATA'] == dia)])
                soma += qtd
            money += soma
        return money

    def Converte(self):
        linhas = []
        money = self.money()
        atual = {'DPT': 0}
        for dia in self.dias:
            total_dia = 0
            for cc in self.centros:
                qtd = len(self.departamento[(self.departamento['C.C'] == cc) & (self.departamento['DATA'] == dia)])
                total_dia += qtd
            atual[dia] = total_dia
        total = 0
        for i in atual:
            total += atual[i]
        atual['Total'] = total
        atual['Valor total'] = f'{money * 20:.2f}'
        pct = []
        for cc in self.centros:
            nova_linha = {'DPT': cc}
            soma = 0
            for dia in self.dias:
                qtd = len(self.departamento[(self.departamento['C.C'] == cc) & (self.departamento['DATA'] == dia)])
                nova_linha[dia] = qtd
                soma += qtd
            valor = float(f'{(soma * 20) / float(atual['Valor total']):.2f}')
            nova_linha['%'] = f'%{valor}'
            pct.append(valor)
            nova_linha['Total'] = soma
            nova_linha['Valor total'] = f'R$ {soma * 20:.2f}'
            self.relatorio = pd.concat([self.relatorio, pd.DataFrame([nova_linha])], ignore_index=True)
        
        atual['%'] = f'%{sum(pct) * 100}'
        self.relatorio = pd.concat([self.relatorio, pd.DataFrame([atual])], ignore_index=True)
        self.relatorio = pd.concat([self.relatorio, pd.DataFrame([linhas])], ignore_index=True)
        self.relatorio.to_csv(r'CSV_ARQ\relatorio_atualizado.csv', index=False, encoding='latin1')
        self.relatorio.to_excel(r"EXCEL_ARQ\relatorio_atualizado.xlsx", index=False)