from django.db import models

class Kelas(models.Model):
    nama = models.TextField(max_length=10)

    def __str__(self):
        return self.nama

class Keterangan(models.Model):
    nama = models.CharField(max_length=4)
    keterangan = models.TextField()

    def __str__(self):
        return self.nama

class Data(models.Model):
    nis = models.CharField(max_length=8)
    nama = models.CharField(max_length=50)
    kelas_id = models.ForeignKey(Kelas, on_delete=models.CASCADE, null=True)
    keterangan_id = models.ForeignKey(Keterangan, on_delete=models.CASCADE, null=True)
    jabatan = models.CharField(max_length=50)
    cover = models.ImageField(upload_to='cover/', null=True)
    tanggal = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.nama