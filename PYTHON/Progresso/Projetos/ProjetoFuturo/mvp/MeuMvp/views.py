from django.core.files.storage import default_storage
from django.conf import settings
from django.shortcuts import render
from .services import *

# Create your views here.

def clase(request):
    relatorio = relatorioValores = None
    
    if request.method == 'POST':
        post = request.FILES['ArquivoCsv']
        fileDS = default_storage.save(f'{post}',post)
        path = os.path.join(f'{settings.MEDIA_ROOT}\{fileDS}')
        Files = Relatorios(path)
        Geral, Financeiro = Files.Separa()
        relatorio = f'{settings.MEDIA_URL}{Geral}'
        relatorioValores = f'{settings.MEDIA_URL}{Financeiro}'
        
    return render(request, 'mvp/index.html', {
            'relatorio': relatorio,
            'relatorioVALORES': relatorioValores
    }
                  )