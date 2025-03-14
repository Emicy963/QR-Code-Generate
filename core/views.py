from django.shortcuts import render

def generete_qr_code(request):
    return render(request, 'generete_qr_code.html')
