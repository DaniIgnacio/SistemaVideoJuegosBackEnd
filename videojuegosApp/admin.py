from django.contrib import admin
from .models import *
from django.contrib.auth.models import Permission

# Register your models here.
class EmpresaAdmin(admin.ModelAdmin):
    list_display=['nombre','pais','correo','fecha_fundacion']

class JuegosAdmin(admin.ModelAdmin):
    list_display=['nombre','foto','genero','lanzamiento','id_empresa']

admin.site.register(Empresa, EmpresaAdmin)
admin.site.register(Juego, JuegosAdmin)
admin.site.register(Permission)
