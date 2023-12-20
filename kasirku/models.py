from django.db import models


class Barang(models.Model):
    barang = models.CharField(max_length=50)
    kode = models.CharField(max_length=40)
    harga = models.FloatField(null=True)
    quantity = models.IntegerField()
    
    def __str__(self):
        return self.barang
