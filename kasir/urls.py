from django.contrib import admin
from django.urls import path
from kasirku.views import *
from django.contrib.auth.views import LoginView, LogoutView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('buku/', buku, name='buku'),
    path('barang/', barang, name='barang'),
    path('masuk/', LoginView.as_view(), name='masuk'),
    path('dashboard/', dashboard, name='dashboard'),
    path('keluar/', LogoutView.as_view(next_page='masuk'), name='keluar'),
    path('add/<int:product_id>/', add_cart, name='add_cart'),
    path('remove/<int:product_id>/', remove_cart, name='remove_cart'),
    path('clear/', clear_cart, name='clear_cart'),
]
