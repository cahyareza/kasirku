from django.shortcuts import render, redirect, get_object_or_404
from kasirku.models import Barang
from django.contrib.auth import authenticate, login, logout
from .forms import FormLogin, CartAddProductForm
from django.contrib.auth.decorators import login_required
from django.conf import settings
from django.views.decorators.http import require_POST
from .cart import Cart


@login_required(login_url=settings.LOGIN_URL)
def buku(request):
    barangs = Barang.objects.all()
    
    konteks = {
        'barangs' : barangs,
    }
    return render(request, 'buku.html', konteks, )

@login_required(login_url=settings.LOGIN_URL)
def barang(request):
    barangs = Barang.objects.all()
    tittle = "Daftar Barang";
    cart_product_form = CartAddProductForm()
    cart = Cart(request)
    
    konteks = {
        'barangs' : barangs,
        'tittle' : tittle,
        'cart_product_form': cart_product_form,
        'cart': cart,
    }
    return render(request, 'barang.html', konteks, )

@login_required(login_url=settings.LOGIN_URL)
def dashboard(request):
    barangs = Barang.objects.all()
    tittle = "Daftar Barang";
    
    konteks = {
        'barangs' : barangs,
        'tittle' : tittle,
    }
    return render(request, 'dashboard.html', konteks )

def login_view(request):
    form = FormLogin()
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            return redirect('/dashboard')
        
    return render(request, 'login.html', {'form':form})

def logout_view(request):
    logout(request)
    request.session.flush()
    return redirect('login')


@require_POST
def add_cart(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Barang, id=product_id)
    form = CartAddProductForm(request.POST)
    if form.is_valid():
        cd=form.cleaned_data
        cart.add(product=product, quantity=cd['quantity'], override_quantity=cd['override'])

    return redirect('barang')


def remove_cart(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Barang, id=product_id)
    cart.remove(product=product)
    return redirect('barang')


def clear_cart(request):
    cart = Cart(request)
    cart.clear()
    return render(request, 'cart/success.html')
    
