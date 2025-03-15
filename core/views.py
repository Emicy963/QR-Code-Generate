from django.shortcuts import render
from .forms import QRCodeForm
import qrcode


def generete_qr_code(request):
    if request.method == 'POST':
        form = QRCodeForm(request.POST)
        if form.is_valid():
            res_name = form.cleaned_data['restaurant_name']
            url = form.cleaned_data['url']

            # Generate QR Code
            qr = qrcode.make(url)
            file_name = res_name.replace(" ", "_").lower() + '_menu.png'
            qr.save(file_name)
        #return
    elif request.method == 'GET':
        form = QRCodeForm()
        context = {
            'form': form
        }
        return render(request, 'generete_qr_code.html', context)
