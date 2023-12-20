from django.forms import ModelForm
from kasirku.models import Barang
from django import forms
from django.contrib.auth.models import User

class FormLogin(forms.Form):
    username = forms.CharField(
        widget=forms.TextInput(attrs={'class':'form-control-lg','type':'text'}),
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'class':'form-control-lg'}),
    )


class CartAddProductForm(forms.Form):
    quantity = forms.IntegerField(initial=1, widget=forms.HiddenInput)
    override = forms.BooleanField(required=False, initial=False, widget=forms.HiddenInput)

