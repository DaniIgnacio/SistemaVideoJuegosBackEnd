from django.shortcuts import render, redirect
from .models import *
from .forms import *
from django.conf import settings
import os
from .serializers import *
from django.shortcuts import get_object_or_404, redirect, render
from http import server

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

def listadoJuegos(request):
    juegos = Juego.objects.all()
    data = {'juegos': juegos}
    return render(request, 'videoJuego.html', data)

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






from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

@api_view(['GET','POST'])
def listado_empresa(request):
    if request.method=='GET':
        empresas=Empresa.objects.all()#.order_by("fecha")
        ser=EmpresaSerializer(empresas,many=True)
        return Response(ser.data)
    if request.method=='POST':
        ser=EmpresaSerializer(data=request.data)
        if ser.is_valid():
            ser.save()
            return Response(ser.data,status=status.HTTP_201_CREATED)
        return Response(ser.errors,status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET','PUT','DELETE'])
def empresas_detail(request,pk):
    try:
        empresa=Empresa.objects.get(pk=pk)
    except:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method =='GET':
        ser=EmpresaSerializer(empresa)
        return Response(ser.data)
    if request.method =='PUT':
        ser=EmpresaSerializer(empresa,data=request.data)
        if ser.is_valid():
            ser.save()
            return Response(ser.data)
        return Response(ser.errors,status=status.HTTP_400_BAD_REQUEST)
    if request.method =='DELETE':
        empresa.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    



@api_view(['GET','POST'])
def listado_juego(request):
    if request.method=='GET':
        juegos=Juego.objects.all()#.order_by("fecha")
        ser=JuegoSerializer(juegos,many=True)
        return Response(ser.data)
    if request.method=='POST':
        ser=JuegoSerializer(data=request.data)
        if ser.is_valid():
            ser.save()
            return Response(ser.data,status=status.HTTP_201_CREATED)
        return Response(ser.errors,status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET','PUT','DELETE'])
def juegos_detalles(request,pk):
    try:
        juego=Juego.objects.get(pk=pk)
    except:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method =='GET':
        ser=JuegoSerializer(juego)
        return Response(ser.data)
    if request.method =='PUT':
        ser=JuegoSerializer(juego,data=request.data)
        if ser.is_valid():
            ser.save()
            return Response(ser.data)
        return Response(ser.errors,status=status.HTTP_400_BAD_REQUEST)
    if request.method =='DELETE':
        juego.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)