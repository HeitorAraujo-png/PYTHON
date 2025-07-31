from django.core.files.storage import default_storage
from django.conf import settings
from django.shortcuts import render
from .services import *

# Create your views here.

def Geracao(request):
    relatorio = relatorioValores = None
    
    if request.method == 'POST':
        post = request.FILES['ArquivoCsv']
        fileDS = default_storage.save(f'{post}',post)
        nome = post
        path = os.path.join(f'{settings.MEDIA_ROOT}\{fileDS}')
        Files = Geral(path, nome)
        if Files.MakeArq():
            relatorio = 'erro'
        
        relatorio = Files.Tratamento()
        relatorioValores = f'{settings.MEDIA_URL}{Financeiro}'
        
    return render(request, 'mvp/index.html', {
            'relatorio': f'{settings.MEDIA_URL}{relatorio}' if relatorio else '',
            'relatorioVALORES': relatorioValores
    }
                  )