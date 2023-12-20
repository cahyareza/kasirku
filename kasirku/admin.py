from django.contrib import admin
from kasirku.models import Barang

class BarangAdmin(admin.ModelAdmin):
    list_display = [ 'barang','kode', 'harga', 'quantity']
    search_fields = ['barang','kode', 'harga', 'quantity']
    # list_filter = ('kelompok_id',)
    list_per_page = 10

admin.site.register(Barang, BarangAdmin)