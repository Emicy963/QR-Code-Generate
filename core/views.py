from django.shortcuts import render
from .forms import QRCodeForm
import qrcode
import os
from django.conf import settings


def generete_qr_code(request):
    if request.method == 'POST':
        form = QRCodeForm(request.POST)
        if form.is_valid():
            res_name = form.cleaned_data['restaurant_name']
            url = form.cleaned_data['url']

            # Generate QR Code
            qr = qrcode.make(url)
            file_name = res_name.replace(" ", "_").lower() + '_menu.png'
            file_path = os.path.join(settings.MEDIA_ROOT, file_name) #../media/exemplo_menu.png
            qr.save(file_path)

            # Create image url
            qr_url = os.path.join(settings.MEDIA_URL, file_name)
            print('media url-', qr_url)

            context = {
                'res_name': res_name.title(),
                'qr_url': qr_url,
            }
            return render(request, 'qr_result.html', context)
    elif request.method == 'GET':
        form = QRCodeForm()
        context = {
            'form': form
        }
        return render(request, 'generete_qr_code.html', context)
