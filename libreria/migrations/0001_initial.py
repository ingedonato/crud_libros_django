# Generated by Django 4.1.7 on 2023-03-27 14:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Libro',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('titulo', models.CharField(max_length=100)),
                ('imagen', models.ImageField(blank=True, null=True, upload_to='imagenes/')),
            ],
        ),
    ]
