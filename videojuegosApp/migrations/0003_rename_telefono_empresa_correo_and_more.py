# Generated by Django 4.2.7 on 2023-11-26 23:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('videojuegosApp', '0002_alter_juego_foto'),
    ]

    operations = [
        migrations.RenameField(
            model_name='empresa',
            old_name='telefono',
            new_name='correo',
        ),
        migrations.RenameField(
            model_name='empresa',
            old_name='fehca_fundacion',
            new_name='fecha_fundacion',
        ),
        migrations.RenameField(
            model_name='empresa',
            old_name='direccion',
            new_name='pais',
        ),
    ]
