from django.shortcuts import render, redirect
from .models import Pessoa
import pandas as pd
import os
from .services import Relatorio

def upload_view(request):
    output_url = None

    if request.method == 'POST':
        rel1 = request.FILES['relatorio1']
        rel2 = request.FILES['relatorio2']

        relatorio = Relatorio(rel1, rel2)
        output_url = relatorio.Converte()

    return render(request, 'uploadapp/upload.html', {'output_url': output_url})