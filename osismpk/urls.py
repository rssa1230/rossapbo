from django.contrib import admin
from django.urls import path
from pengurus.views import *


urlpatterns = [
    path('admin/', admin.site.urls),
    path('data/', data),
    path('tambah-data/', tambah_data),
    path('data/ubah/<int:id_data>', ubah_data, name='ubah_data'),
]
