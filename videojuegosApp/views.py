from django.shortcuts import render, redirect
from .models import *
from .forms import *
from django.conf import settings
import os

# Create your views here.
def home(request):
    return render(request,'index.html')

def listadoEmpresa(request):
    empresas = Empresa.objects.all()
    data = {'empresas': empresas}
    return render(request, 'empresa.html',data)

def agregarEmpresa(request):
    form = FormEmpresa()
    if request.method == 'POST':
        form = FormEmpresa(request.POST)
        if form.is_valid():
            form.save()
            return redirect(listadoEmpresa)
    data = {'form': form}
    return render(request, 'agregarEmpresa.html', data)

def eliminarEmpresa(request, id):
    empresa = Empresa.objects.get(id=id)
    juegos_empresa = Juego.objects.filter(id_empresa=empresa)
    for juego in juegos_empresa:
        ruta_imagen = os.path.join(settings.MEDIA_ROOT, str(juego.foto))
        if os.path.isfile(ruta_imagen):
            os.remove(ruta_imagen)
        juego.delete()

    # Finalmente, elimina la empresa
    empresa.delete()

    return redirect('/empresas')
def editarEmpresa(request,id):
    empresa = Empresa.objects.get(id = id)
    form = FormEmpresa(instance=empresa)
    if request.method == 'POST':
        form = FormEmpresa(request.POST, instance=empresa)
        if form.is_valid():
            form.save()
        return redirect("/empresas")
    data = {'form': form}
    return render(request,'agregarEmpresa.html',data)



def listadoJuegos(request):
    juegos = Juego.objects.all()
    data = {'juegos': juegos}
    return render(request, 'videoJuego.html', data)

def agregarJuegos(request):
    form = FormJuego()
    if request.method == 'POST':
        form = FormJuego(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect(listadoJuegos)
    data = {'form': form}
    return render(request, 'agregarJuego.html', data)

def eliminarJuego(request, id):
    juego = Juego.objects.get(id=id)
    ruta_imagen = os.path.join(settings.MEDIA_ROOT, str(juego.foto))
    juego.delete()
    if os.path.isfile(ruta_imagen):
        os.remove(ruta_imagen)

    return redirect('/videojuegos')
def editarJuego(request,id):
    juego = Juego.objects.get(id = id)
    form = FormJuego(instance=juego)
    if request.method == 'POST':
        form = FormJuego(request.POST, instance=juego)
        if form.is_valid():
            form.save()
        return redirect("/videojuegos")
    data = {'form': form}
    return render(request,'agregarJuego.html',data)
