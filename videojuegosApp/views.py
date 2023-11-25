from django.shortcuts import render, redirect
from .models import *
from .forms import *

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
            return listadoEmpresa(request)
    data = {'form': form}
    return render(request, 'agregarEmpresa.html', data)

def eliminarEmpresa(request,id):
    empresa = Empresa.objects.get(id = id)
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



def listadoAlumnos(request):
    juegos = Juego.objects.all()
    data = {'juegos': juegos}
    return render(request, 'videoJuego.html', data)

def agregarJuegos(request):
    form = FormJuego()
    if request.method == 'POST':
        form = FormJuego(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return listadoAlumnos(request)
    data = {'form': form}
    return render(request, 'agregarJuego.html', data)

def eliminarJuego(request,id):
    juego = Juego.objects.get(id = id)
    juego.delete()
    return redirect('/videojuegos')

def editarJuego(request,id):
    empresa = Empresa.objects.get(id = id)
    form = FormEmpresa(instance=empresa)
    if request.method == 'POST':
        form = FormEmpresa(request.POST, instance=empresa)
        if form.is_valid():
            form.save()
        return redirect("/empresas")
    data = {'form': form}
    return render(request,'agregarEmpresa.html',data)
