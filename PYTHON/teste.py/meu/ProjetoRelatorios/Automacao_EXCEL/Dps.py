import pandas as pd
                
class Relatorio:
    
    def __init__(self):
        self.Converter()
        self.LinkPathPTD = r'RelatoriosMensaisCSV\DPTDIA.csv'
        self.departamento = pd.read_csv(self.LinkPathPTD, encoding='latin1')
        self.replace()
        self.dias = self.Dias()
        self.centros = self.CentroCustos()
        self.LinkPathRelatorio = r'CSV_ARQ\relatorio.csv'
        self.relatorio = pd.read_csv(self.LinkPathRelatorio, encoding='latin1')
        
    def Converter(self):
        relatorio1 = pd.read_excel(r'RelatoriosMensaisEXCEL\Dptdia1-15.xltx', parse_dates=["DATA"])
        relatorio2 = pd.read_excel(r'RelatoriosMensaisEXCEL\Dptdia16-31.xlsx', parse_dates=["DATA"])
        relatorio1['DATA'] = relatorio1['DATA'].dt.strftime('%d/%m/%y')
        relatorio2['DATA'] = relatorio2['DATA'].dt.strftime('%d/%m/%y')
        relatorio1.to_csv(r'CSV_ARQ\DPT\DPT01-15.csv', index=False)
        relatorio2.to_csv(r'CSV_ARQ\DPT\DPT16-31.csv', index=False)
        relatorio = pd.concat([relatorio1, relatorio2], ignore_index=True)
        relatorio.to_csv(r'RelatoriosMensaisCSV\DPTDIA.csv')   

    def replace(self):
        with open(self.LinkPathPTD, 'r', encoding='latin1') as arq:
            if ';' in arq.read():
                with open(self.LinkPathPTD, 'w', encoding='latin1') as csv:
                    arq = arq.read()
                    for line in arq:
                        csv.write(line.replace(';', ','))
        
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
        centro = self.departamento['C.C']
        centro = self.remove(list(centro))
        lista = []
        for i in range(0, len(centro)):
            pre = str(centro[i])
            ic = f'{''.join((pre[0], pre[1]))}'
            cc = f'{''.join((pre[2], pre[3]))}'
            if ic == '81':
                lc = 'TVCA'
            if ic == '65':
                lc = 'Portal MT'
            if ic == '69':
                lc = 'FMCA'
            if ic == '85':
                lc = 'On Line(MT)'
            if cc == '03':
                lista.append(f'{centro[i]} - ADM - {lc}')
            if cc == '06':
                lista.append(f'{centro[i]} - RH - {lc}')
            if cc == '10':
                lista.append(f'{centro[i]} - COMERCIA - {lc}')
            if cc == '11':
                lista.append(f'{centro[i]} - OPEC - {lc}')
            if cc == '14':
                lista.append(f'{centro[i]} - PROGRAMAÇÃO - {lc}')
            if cc == '15':
                lista.append(f'{centro[i]} - JORNALISMO - {lc}')
            if cc == '21':
                lista.append(f'{centro[i]} - TECNOLOGIA - {lc}')
        return self.remove(lista)

    def money(self):
        money = 0
        for cc in self.centros:
            for i in range(0, 1):
                nm = f'{''.join((cc[0], cc[1], cc[2], cc[3]))}'
                cc = int(nm)
            soma = 0
            for dia in self.dias:
                qtd = len(self.departamento[(self.departamento['C.C'] == cc) & (self.departamento['DATA'] == dia)])
                soma += qtd
            money += soma
        return money

    def Converte(self):
        self.Add()
        linhas = []
        money = self.money()
        atual = {'DPT': 0}
        for dia in self.dias:
            total_dia = 0
            for cc in self.centros:
                for i in range(0, 1):
                    nm = f'{''.join((cc[0], cc[1], cc[2], cc[3]))}'
                    cc = int(nm)
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
            for i in range(0, 1):
                nm = f'{''.join((cc[0], cc[1], cc[2], cc[3]))}'
                cc = int(nm)
            soma = 0
            for dia in self.dias:
                qtd = len(self.departamento[(self.departamento['C.C'] == cc) & (self.departamento['DATA'] == dia)])
                nova_linha[dia] = qtd
                soma += qtd
            valor = float(f'{(soma * 20) / float(atual['Valor total']):.3f}')
            nova_linha['%'] = f'{valor}%'
            pct.append(valor)
            nova_linha['Total'] = soma
            nova_linha['Valor total'] = f'R$ {soma * 20:.2f}'
            self.relatorio = pd.concat([self.relatorio, pd.DataFrame([nova_linha])], ignore_index=True)
        
        atual['%'] = f'%{sum(pct) * 100}'
        self.relatorio = pd.concat([self.relatorio, pd.DataFrame([atual])], ignore_index=True)
        self.relatorio = pd.concat([self.relatorio, pd.DataFrame([linhas])], ignore_index=True)
        self.relatorio.to_csv(r'CSV_ARQ\relatorio_atualizado.csv', index=False, encoding='latin1')
        self.relatorio.to_excel(r"relatorio_atualizado.xlsx", index=False)