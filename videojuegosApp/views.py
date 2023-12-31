from django.shortcuts import render, redirect
from .models import *
from .forms import *
from django.conf import settings
import os
from .serializers import *
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.decorators import login_required,permission_required
from django.http import HttpResponseForbidden
from django.contrib.auth.views import LoginView


# Create your views here.
@login_required()
def home(request):
    return render(request,'index.html')


@login_required(login_url='/admin/login/')
@permission_required('videojuegosApp.view_empresa')
def listadoEmpresa(request):
    empresas = Empresa.objects.all()
    data = {'empresas': empresas}
    return render(request, 'empresa.html', data)

@login_required(login_url='/admin/login/')
@permission_required('videojuegosApp.add_empresa')
def agregarEmpresa(request):
    form = FormEmpresa()
    if request.method == 'POST':
        form = FormEmpresa(request.POST)
        if form.is_valid():
            form.save()
            return redirect(listadoEmpresa)
    data = {'form': form}
    return render(request, 'agregarEmpresa.html', data)


@login_required(login_url='/admin/login/')
@permission_required('videojuegosApp.delete_empresa')
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

@login_required(login_url='/admin/login/')
@permission_required('videojuegosApp.change_empresa')
def editarEmpresa(request, id):
    empresa = get_object_or_404(Empresa, id=id)

    if request.method == 'POST':
        form = FormEmpresa(request.POST, instance=empresa)
        if form.is_valid():
            form.save()
            return redirect("/empresas")  # Cambia esto a tu URL de lista de empresas
    else:
        form = FormEmpresa(instance=empresa)  # Rellenar formulario con datos de la empresa

    data = {'form': form}
    return render(request, 'agregarEmpresa.html', data)


@login_required(login_url='/admin/login/')
@permission_required('videojuegosApp.view_juego')
def listadoJuegos(request):
    juegos = Juego.objects.all()
    data = {'juegos': juegos}
    return render(request, 'videoJuego.html', data)

@login_required(login_url='/admin/login/')
@permission_required('videojuegosApp.add_juego')
def agregarJuegos(request):
    if request.method == 'POST':
        form = FormJuego(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect(listadoJuegos)
    else:  # GET request o formulario no válido
        form = FormJuego()

    data = {'form': form}
    return render(request, 'agregarJuego.html', data)

@login_required(login_url='/admin/login/')
@permission_required('videojuegosApp.delete_juego')
def eliminarJuego(request, id):
    juego = Juego.objects.get(id=id)
    ruta_imagen = os.path.join(settings.MEDIA_ROOT, str(juego.foto))
    juego.delete()
    if os.path.isfile(ruta_imagen):
        os.remove(ruta_imagen)

    return redirect('/videojuegos')
def editarJuego(request, id):
    juego = get_object_or_404(Juego, id=id)
    imagen_antigua = juego.foto

    if request.method == 'POST':
        form = FormJuego(request.POST, request.FILES, instance=juego)
        if form.is_valid():
            nueva_imagen = form.cleaned_data['foto']
            if nueva_imagen != imagen_antigua:  
                juego.foto = nueva_imagen
                if imagen_antigua:
                    
                    ruta_imagen_antigua = os.path.join(settings.MEDIA_ROOT, str(imagen_antigua))
                    if os.path.isfile(ruta_imagen_antigua):
                        os.remove(ruta_imagen_antigua)
            else:
                
                juego.foto = imagen_antigua

            form.save()
            return redirect("/videojuegos")
    else:
        form = FormJuego(instance=juego)
        form.fields['lanzamiento'].initial = juego.lanzamiento.strftime('%Y-%m-%d') if juego.lanzamiento else None

    data = {'form': form}
    return render(request, 'agregarJuego.html', data)






from rest_framework import viewsets


class EmpresasList(viewsets.ModelViewSet):
    queryset = Empresa.objects.all()
    serializer_class = EmpresaSerializer

class JuegosList(viewsets.ModelViewSet):
    queryset = Juego.objects.all()
    serializer_class = JuegoSerializer


