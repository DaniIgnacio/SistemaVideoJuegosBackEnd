from .models  import *
from django import forms


class FormEmpresa(forms.ModelForm):
    class Meta:
        model = Empresa
        fields = '__all__'

        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'direccion': forms.TextInput(attrs={'class': 'form-control'}),
            'telefono': forms.TextInput(attrs={'class': 'form-control'}),
            'fecha_fundacion': forms.DateInput(attrs={'class': 'form-control'}),
        }


class FormJuego(forms.ModelForm):
    class Meta:
        model = Juego
        fields = '__all__'

    nombre = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    foto = forms.ImageField()
    genero = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    lanzamiento = forms.DateField(widget=forms.DateInput(attrs={'class': 'form-control'}))
    id_empresa = forms.ModelChoiceField(queryset=Empresa.objects.all(), widget=forms.Select(attrs={'class': 'form-control'}))