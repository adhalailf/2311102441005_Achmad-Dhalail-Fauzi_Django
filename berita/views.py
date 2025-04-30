from django.shortcuts import render, redirect
from berita.models import Kategori, Artikel
from berita.forms import ArtikelForm

# Create your views here.
def dashboard(request):
    template_name = 'dashboard/index.html'
    context = {
        'title': 'Halaman Dashboard',
    }
    return render(request, template_name, context)

def kategori_list(request):
    template_name = 'dashboard/content/kategori_list.html'
    kategori = Kategori.objects.all()
    print= (kategori)
    context = {
        'title': 'Halaman Kategori',
        'kategori': kategori,
    }
    return render(request, template_name, context)

def kategori_add(request):
    template_name = 'dashboard/content/kategori_add.html'
    if request.method == 'POST':
        nama_input = request.POST.get('nama_kategori')
        Kategori.objects.create(
            nama=nama_input
        )
        return redirect('kategori_list')
    
    pesan = ""
    context = {
        'title': 'Tambah Kategori',
        'pesan' : pesan,
    }
    return render(request, template_name, context)

def kategori_upt(request, id_kat):
    template_name = 'dashboard/content/kategori_upt.html'
    try:
        kategori = Kategori.objects.get(id=id_kat)
    except:
        return redirect(kategori_list)
    if request.method == 'POST':
        nama_input = request.POST.get('nama_kategori')
        kategori.nama = nama_input
        kategori.save()
        return redirect('kategori_list')
    context = {
        'title': 'Ubah Kategori',
        'kategori': kategori,
    }
    return render(request, template_name, context)

def kategori_del(request, id_kat):
    try:
        Kategori.objects.get(id=id_kat).delete()
    except:
        pass
    return redirect(kategori_list)

def artikel_list(request):
    template_name = 'dashboard/content/artikel_list.html'
    artikel = Artikel.objects.all()
    print = (artikel)
    context = {
        'title': 'Daftar Artikel',
        'artikel': artikel,
    }
    return render(request, template_name, context)

def artikel_add(request):
    template_name = 'dashboard/content/artikel_forms.html'
    if request.method == 'POST':
        forms = ArtikelForm(request.POST, request.FILES)
        if forms.is_valid():
            pub = forms.save (commit=False)
            pub.author = request.user
            pub.save()
            return redirect(artikel_list)
        else:
            print(forms.error_class)
    forms = ArtikelForm()
    context = {
        'title': 'Tambah Artikel',
        'forms': forms,
        
    }
    return render(request, template_name, context)

def artikel_detail(request, id_art):
    template_name = 'dashboard/content/artikel_detail.html'
    artikel = Artikel.objects.get(id=id_art)
    context = {
        'title': artikel.judul,
        'artikel': artikel,
    }
    return render(request, template_name, context)

def artikel_upt(request, id_art):
    template_name = 'dashboard/content/artikel_forms.html'
    artikel = Artikel.objects.get(id=id_art)
    if request.method == 'POST':
        forms = ArtikelForm(request.POST, request.FILES, instance=artikel)
        if forms.is_valid():
            pub = forms.save(commit=False)
            pub.author = request.user
            pub.save()
            return redirect(artikel_list)
    forms = ArtikelForm(instance=artikel)
    context = {
        'title': 'Ubah Artikel',
        'forms': forms,
    }
    return render(request, template_name, context)

def artikel_del(request, id_art):
    try:
        Artikel.objects.get(id=id_art).delete()
    except:
        pass
    return redirect(artikel_list)