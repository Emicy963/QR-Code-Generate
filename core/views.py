from django.shortcuts import render
from .forms import QRCodeForm


def generete_qr_code(request):
    if request.method == 'POST':
        form = QRCodeForm(request.POST)
        if form.is_valid():
            res_name = form.cleaned_data['restaurant_name']
            url = form.cleaned_data['url']
        return
    elif request.method == 'GET':
        form = QRCodeForm()
        context = {
            'form': form
        }
        return render(request, 'generete_qr_code.html', context)
