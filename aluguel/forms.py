from django import forms
from .models import Carro, Cliente

class CarroForm(forms.ModelForm):
    class Meta:
        model = Carro
        fields = ['modelo', 'ano', 'placa', 'disponivel']

class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ['nome', 'email']


