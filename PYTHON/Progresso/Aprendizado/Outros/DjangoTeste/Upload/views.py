from django.shortcuts import render
from .services import *
from django.conf import settings
# Create your views here.
def qrcode(request):
    img = None

    if request.method == 'POST':
        nome = request.POST.get('nome')
        link = request.POST.get('link')
        codeqr = QR(nome)
        img = codeqr.qr(link)
    if img == None:
        return render(request, 'Upload/index.html')
    else:
        return render(request, 'Upload/index.html', {'out': f'{settings.MEDIA_URL}{img}'})