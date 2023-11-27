from .models  import *
from django import forms
from django.forms.widgets import SelectDateWidget


class FormEmpresa(forms.ModelForm):
    class Meta:
        model = Empresa
        fields = '__all__'

        
    nombre = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    pais = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    correo= forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    fecha_fundacion= forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))

class DateInput(forms.DateInput):
    input_type = 'date'
    format = '%Y-%m-%d'


class FormJuego(forms.ModelForm):
    class Meta:
        model = Juego
        fields = '__all__'

    nombre = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    foto = forms.ImageField()
    genero = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    lanzamiento = forms.DateField(widget=forms.DateInput(attrs={'class': 'form-control'}))
    id_empresa = forms.ModelChoiceField(queryset=Empresa.objects.all(), widget=forms.Select(attrs={'class': 'form-control'}))