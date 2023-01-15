from django.contrib import admin
from django.urls import path
from pengurus.views import *
from django.contrib.auth.views import *
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('data/', data, name='data'),
    path('tambah-data/', tambah_data, name='tambah_data'),
    path('data/ubah/<int:id_data>', ubah_data, name='ubah_data'),
    path('data/hapus/<int:id_data>', hapus_data, name='hapus_data'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
    path('signup/', signup, name='signup'),
    path('export/xls/', export_xls, name='export_xls'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
