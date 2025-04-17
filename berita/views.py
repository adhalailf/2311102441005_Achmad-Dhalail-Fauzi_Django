from django.shortcuts import render

# Create your views here.
def dashboard(request):
    template_name = 'dashboard/index.html'
    context = {
        'title': 'Halaman Dashboard',
    }
    return render(request, template_name, context)
