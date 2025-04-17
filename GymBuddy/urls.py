from django.contrib import admin
from django.urls import path, include

######################## ini untuk menampilkan gambar yang sudah diupload pada folder media ############################
from django.conf import settings
from django.conf.urls.static import static

from GymBuddy.views import home, about
urlpatterns = [
    path("admin/", admin.site.urls),

    path("",  home, name="home"),
    
    path("dashboard/",  include("berita.urls")),
]

######################## ini untuk menampilkan gambar yang sudah diupload pada folder media ############################
if settings.DEBUG: 
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)