from django.core.files.storage import default_storage
from django.conf import settings
import qrcode
from pyzbar import pyzbar
from PIL import Image
import os
class QR:
    
    def __init__(self, nome):
        if not nome.endswith('.png'):
            nome = f'{nome}.png'
        nome = ''.join(nome.split())
        self.nome = nome
        if os.path.exists((os.path.join(settings.MEDIA_ROOT, f'qrcodes/{self.nome}'))):
            os.remove((os.path.join(settings.MEDIA_ROOT, f'qrcodes/{self.nome}')))
            
    def qr(self, link):
        
        qr = qrcode.make(link, box_size=5, border=0)
        qr.save((os.path.join(settings.MEDIA_ROOT, f'qrcodes\{self.nome}')))
        return f'qrcodes/{self.nome}'
    
class Pyz:
    
    def __init__(self, arq):
        self.arq = arq
        
    def leitura(self):
        try:
            image = Image.open(os.path.join(settings.MEDIA_ROOT, self.arq))
        except:
            return 'Arquivo incompativel'
        decodeqr = pyzbar.decode(image)
        if decodeqr:
            lista = []
            for i in decodeqr:
                return f'Dados do QRCODE: \n{i.data.decode('utf-8')}'
        else:
            return 'erro'
    
    def limpa(self):
        if os.path.exists(os.path.join(settings.MEDIA_ROOT, self.arq)):
            os.remove(os.path.join(settings.MEDIA_ROOT, self.arq))