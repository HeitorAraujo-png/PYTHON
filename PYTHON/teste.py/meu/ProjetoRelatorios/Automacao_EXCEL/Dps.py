import pandas as pd
                
class Relatorio:
    
    def __init__(self):
        self.LinkPathPTD = r'CSV_ARQ\Dptdia.csv'
        self.LinkPathRelatorio = r'CSV_ARQ\relatorio.csv'
        self.departamento = pd.read_csv(self.LinkPathPTD, encoding='latin1')
        self.dias = self.Dias()
        self.Add()
        self.centros = self.CentroCustos()
        self.relatorio = pd.read_csv(self.LinkPathRelatorio, encoding='latin1')

    def replace(self):
        with open(self.LinkPathPTD, 'r', encoding='latin1') as arq:
            arq = arq.read()
            with open(self.LinkPathPTD, 'w', encoding='latin1') as csv:
                for i in arq:
                    csv.write(arq.replace(';', ','))
        
    def Add(self):
        with open(self.LinkPathRelatorio, 'r', encoding='latin1') as arq:
            arq = arq.readlines()
            with open(self.LinkPathRelatorio, 'w', encoding='latin1') as csv:
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