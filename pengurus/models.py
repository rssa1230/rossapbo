from django.db import models

class Keterangan(models.Model):
    nama = models.CharField(max_length=4)
    keterangan = models.TextField()

    def __str__(self):
        return self.nama

class Data(models.Model):
    nis = models.CharField(max_length=8)
    nama = models.CharField(max_length=50)
    kelas = models.CharField(max_length=50)
    keterangan_id = models.ForeignKey(Keterangan, on_delete=models.CASCADE, null=True)
    jabatan = models.CharField(max_length=50)

    def __str__(self):
        return self.nama