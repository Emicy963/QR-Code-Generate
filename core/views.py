from django.shortcuts import render
from .forms import QRCodeForm


def generete_qr_code(request):
    form = QRCodeForm()
    context = {
        'form': form
    }
    return render(request, 'generete_qr_code.html', context)
