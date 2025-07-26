from django.core.files.storage import default_storage
from django.conf import settings
import hashlib
import qrcode
import os
class QR:
    
    def __init__(self, nome):
        if not nome.endswith('.png'):
            nome = f'{nome}.png'
        nome = ''.join(nome.split())
        self.nome = nome
        if os.path.exists((os.path.join(settings.MEDIA_ROOT, self.nome))):
            os.remove((os.path.join(settings.MEDIA_ROOT, self.nome)))
            
    def qr(self, link):
        qr = qrcode.make(link)
        qr.save((os.path.join(settings.MEDIA_ROOT, self.nome)))
        return self.nome