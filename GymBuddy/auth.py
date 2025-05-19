from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User

def acc_login(request):
    ## Jika user sudah login, redirect ke halaman home
    if request.user.is_authenticated:
        return redirect('/')
    template_name = 'halaman/login.html'
    msg = ""
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        print(username, password)
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)    
            return redirect('/')
        else:
            msg = "Login Gagal, Silahkan coba lagi"
    context = {
        'msg': msg,
    }
    return render(request, template_name, context)

def acc_regist(request):
    if request.user.is_authenticated:
        return redirect('/')
    
    pesan = ""
    template_name = 'halaman/regist.html'
    if request.method == 'POST':
        username = request.POST.get('username')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')

        print(username, first_name, last_name, email, password1, password2)
        
        if password1 == password2:
            check_user = User.objects.filter(username=username)
            if check_user.count() == 0:
                user_save = User.objects.create_user(
                    username=username,
                    first_name=first_name,
                    last_name=last_name,
                    email=email,
                    # password=password1,
                    is_active=True
                )
                user_save.set_password(password1)
                user_save.save()
                return redirect('/')
            else:
                pesan = "Username sudah ada, silahkan ganti"
        else:
            pesan = "Password tidak sama"

    context = {
        'pesan': pesan,
    }
    return render(request, template_name, context)

def acc_logout(request):
    logout(request)
    return redirect('/')