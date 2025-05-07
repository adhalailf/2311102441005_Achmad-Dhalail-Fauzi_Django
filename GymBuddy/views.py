#didalam boleh membuat (terdapat banyak) fungsi untuk mengembalikan halaman homepage, login, register, dll
from django.shortcuts import render #render berfungsi untuk mengembalikan halaman html
from berita.models import Artikel, Kategori

def home(request):
    template_name = 'halaman/index.html'
    data_artikel = Artikel.objects.all()
    context = {
        'title': 'Home',
        'data_artikel': data_artikel,
    }
    return render(request, template_name, context) #mengembalikan halaman home.html dengan context yang sudah didefinisikan

def about(request):
    template_name = 'halaman/about.html'
    context = {
        'title': 'About',
        'content': 'About Us!',
        'try' : 2,
    }
    return render(request, template_name, context)

def contact(request):
    template_name = 'halaman/contact.html'
    context = {
        'title': 'Contact',
        'content': 'Contact Us!',
        'try' : 2,
    }
    return render(request, template_name, context)    

def detail_artikel(request, slug):
    template_name = 'halaman/detail_artikel.html'
    artikel = Artikel.objects.get(slug=slug)
    print(artikel)
    context = {
        'title' : artikel.judul,
        'artikel' : artikel,
    }
    return render(request, template_name, context)
