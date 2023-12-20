from django.db import models


class Barang(models.Model):
    barang = models.CharField(max_length=50)
    kode = models.CharField(max_length=40)
    harga = models.FloatField(null=True)
    quantity = models.IntegerField()
    diskon = models.IntegerField()

    @property
    def diskon_value(self):
        value = self.harga * (self.diskon*00.1)
        return value
    
    def __str__(self):
        return self.barang
