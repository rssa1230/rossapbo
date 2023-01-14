from django.contrib import admin
from pengurus.models import *

class DataAdmin(admin.ModelAdmin):
    list_display = ['nis', 'nama', 'kelas', 'jabatan']
    search_fields = ['nis', 'nama', 'kelas', 'jabatan']
    list_filter = ('keterangan_id',)
    list_per_page = 4

admin.site.register(Data, DataAdmin)
admin.site.register(Keterangan)

