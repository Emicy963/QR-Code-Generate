from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.messages import constants
from django.contrib import messages
from django.contrib.auth import login, authenticate, logout

def register_view(request):
    if request.method=='GET':
        return render(request, 'register.html')
    else:
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        password1 = request.POST.get('password1')

        if User.objects.filter(username=username).exists() or User.objects.filter(email=email).exists():
            messages.add_message(request, constants.ERROR, 'Username or Email already exist!')
            return redirect('register')
        elif password!=password1:
            messages.add_message(request, constants.ERROR, "Password don't match!")
            return redirect('register')
        
        try:
            user = User.objects.create_user(
                username=username,
                email=email,
                password=password
            )
            
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                messages.add_message(request, constants.SUCCESS, 'Sucess in Create user!')
                return redirect('generete_qr_code')
            else:
                messages.add_message(request, constants.ERROR, 'Authenticated error!')
                return redirect('register')
        except Exception as err:
            messages.add_message(request, constants.ERROR, f'Error: {str(err)}')
            return redirect('register')
        
def loging_view(request):
    if request.method=='GET':
        return render(request, 'login.html')
    else:
        email = request.POST.get('email')
        password = request.POST.get('password')

        try:
            user = User.objects.get(email=email)
            username = user.username
        except User.DoesNotExist:
            messages.add_message(request, constants.ERROR, 'Invalid Email or Password!')
            return redirect('login')
        
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.add_message(request, constants.SUCCESS, 'Sucess in Login!')
            return redirect('generete_qr_code')
        else:
            messages.add_message(request, constants.ERROR, 'Athenticate erro!')
            return redirect('login')
