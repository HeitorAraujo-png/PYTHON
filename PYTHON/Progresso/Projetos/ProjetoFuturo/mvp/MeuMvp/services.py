import pandas as pd
from openpyxl import *
from django.conf import settings
import os

class Relatorios:
    
    def __init__(self, files):
        self.fileG = self.fileF = pd.read_csv(files)
    
    def Separa(self):
        Geral = 'RelatorioGeral.xlsx'
        Financeiro = 'RelatorioFinanceiro.xlsx'
        self.fileG.to_excel(os.path.join(settings.MEDIA_ROOT, Geral), index=False)
        self.fileF.to_excel(os.path.join(settings.MEDIA_ROOT, Financeiro), index=False)
        return Geral, Financeiro