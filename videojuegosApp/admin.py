from django.contrib import admin
from .models import *

# Register your models here.
class EmpresaAdmin(admin.ModelAdmin):
    list_display=['nombre','pais','correo','fecha_fundacion']

class JuegosAdmin(admin.ModelAdmin):
    list_display=['nombre','foto','genero','lanzamiento','id_empresa']

admin.site.register(Empresa, EmpresaAdmin)
admin.site.register(Juego, JuegosAdmin)