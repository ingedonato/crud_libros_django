# Generated by Django 4.1.7 on 2023-03-27 14:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('libreria', '0002_libro_description_alter_libro_imagen_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='libro',
            old_name='description',
            new_name='descripcion',
        ),
    ]
