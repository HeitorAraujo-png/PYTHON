from django.shortcuts import render
from .services import *
from django.conf import settings

# Create your views here.


def qrcode(request):
    decode = None
    img = None
    if request.method == "POST":
        if "sai" in request.POST:
            img = None
        if "ler" in request.POST:
            qr = request.FILES["arq"]
            arquivo = default_storage.save("leitor/decodar.png", qr)
            dados = Pyz(arquivo)
            decode = dados.leitura()
            dados.limpa()

        elif "nome" in request.POST and "link" in request.POST:
            nome = request.POST.get("nome")
            link = request.POST.get("link")
            codeqr = QR(nome)
            img = codeqr.qr(link)

    return render(
        request,
        "Upload/index.html",
        {"out": f"{settings.MEDIA_URL}{img}" if img else "", "qr": decode},
    )
