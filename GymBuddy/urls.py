from django.contrib import admin
from django.urls import path, include

######################## ini untuk menampilkan gambar yang sudah diupload pada folder media ############################
from django.conf import settings
from django.conf.urls.static import static

from GymBuddy.views import home, about, contact, detail_artikel
from GymBuddy.auth import acc_login, acc_regist, acc_logout


urlpatterns = [
    path("admin/", admin.site.urls),

    path("",  home, name="home"),
    path("about",  about, name="about"),
    path("contact",  contact, name="contact"),
    path("detail/<slug:slug>",  detail_artikel, name="detail_artikel"),
    
    path("dashboard/",  include("berita.urls")),

    path("auth/login",  acc_login, name="acc_login"),
    path("auth/register",  acc_regist, name="acc_regist"),
    path("auth/logout",  acc_logout, name="acc_logout"),
]

######################## ini untuk menampilkan gambar yang sudah diupload pada folder media ############################
if settings.DEBUG: 
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)