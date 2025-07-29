from django.shortcuts import render
import pandas as pd
from .services import Relatorio
from django.conf import settings

def upload_view(request):
    output_url = None

    if request.method == 'POST':
        rel1 = request.FILES['relatorio1']
        rel2 = request.FILES['relatorio2']

        relatorio = Relatorio()
        relatorio.retorna(rel1, rel2)
        output_url = relatorio.Converte()

    return render(request, 'uploadapp/upload.html', {
        'output_url': f'{settings.MEDIA_URL}{output_url}'if output_url else ""}
        )