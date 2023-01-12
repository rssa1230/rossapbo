from django.db import models

class Data(models.Model):
    nama = models.CharField(max_length=50)
    kelas = models.CharField(max_length=50)
    keterangan = models.CharField(max_length=50)
    jabatan = models.CharField(max_length=50)

    def __str__(self):
        return self.nama