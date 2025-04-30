from django.urls import path
from berita.views import (
    dashboard, 
    kategori_list, kategori_add, kategori_upt, kategori_del,
    artikel_list, artikel_add, artikel_detail, artikel_upt, artikel_del)

urlpatterns = [
    
    path("",  dashboard, name="dashboard"),
    path("kategori/list",  kategori_list, name="kategori_list"),
    path("kategori/add", kategori_add, name="kategori_add"),
    path("kategori/upt/<int:id_kat>", kategori_upt, name="kategori_upt"),
    path("kategori/del/<int:id_kat>", kategori_del, name="kategori_del"),
    
    path("artikel/list", artikel_list, name="artikel_list"),
    path("artikel/add", artikel_add, name="artikel_add"),
    path('artikel/detail/<int:id_art>', artikel_detail, name='artikel_detail'),
    path('artikel/upt/<int:id_art>', artikel_upt, name='artikel_upt'),
    path('artikel/del/<int:id_art>', artikel_del, name='artikel_del'),
]


