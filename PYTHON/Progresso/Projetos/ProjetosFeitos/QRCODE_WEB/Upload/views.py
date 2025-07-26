from django.shortcuts import render
from .services import *
from django.conf import settings
# Create your views here.

def qrcode(request):
    img = None
    if request.method == 'POST':
        if 'sai' in request.POST:
            img = None
        else:
            nome = request.POST.get('nome')
            link = request.POST.get('link')
            codeqr = QR(nome)
            img = codeqr.qr(link)
    return render(request, 'Upload/index.html', {'out': f'{settings.MEDIA_URL}{img}' if img else ''})