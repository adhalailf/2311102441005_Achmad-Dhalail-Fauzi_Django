#didalam boleh membuat (terdapat banyak) fungsi untuk mengembalikan halaman homepage, login, register, dll
from django.shortcuts import render #render berfungsi untuk mengembalikan halaman html

def home(request):
    template_name = 'home.html'
    context = {
        'title': 'Home',
        'content': 'Welcome to GymBuddy!',
        'try' : 2,
    }
    return render(request, template_name, context) #mengembalikan halaman home.html dengan context yang sudah didefinisikan

def about(request):
    template_name = 'about.html'
    context = {
        'title': 'About',
        'content': 'About Us!',
        'try' : 2,
    }
    return render(request, template_name, context)