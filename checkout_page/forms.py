from django import forms
from django.forms import ModelForm, TextInput, EmailInput, Select
from checkout_page.models import Checkout, Pengiriman, Pembayaran

class CheckoutForm(forms.ModelForm):
    class Meta:
        model = Checkout
        fields = ['name', 'email', 'telp', 'alamat']
        widgets = {
            'name' : TextInput(attrs={
                'class' : 'form-control',
                'placeholder' : 'Ricardo',
                'required' : ''
            }),
            'email' : EmailInput(attrs={
                'class' : 'form-control',
                'placeholder' : 'ricardo@gmail.com',
                'required' : ''
            }),
            'telp' : TextInput(attrs={
                'class' : 'form-control',
                'placeholder' : '08111751234',
                'required' : ''
            }),
            'alamat' : TextInput(attrs={
                'class' : 'form-control',
                'placeholder' : 'Rumah Ricardo',
                'required' : ''
            }),
        }

class PengirimanForm(forms.ModelForm):
    class Meta:
        model = Pengiriman
        fields = ['durasi', 'kurir']
        widgets = {
            'durasi' : Select(attrs={
                'class' : 'form-control',
                'required' : ''
            }),
            'kurir' : Select(attrs={
                'class' : 'form-control',
                'required' : ''
            }),
        }

class PembayaranForm(forms.ModelForm):
    class Meta:
        model = Pembayaran
        fields = ['metode'] 
        widgets = {
            'metode' : Select(attrs={
                'class' : 'form-control',
                'required' : ''
            }),
        }