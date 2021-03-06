# Generated by Django 2.1.2 on 2018-12-03 01:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Inventario', '0003_auto_20181008_1619'),
        ('Usuario', '0003_remove_usuario_direccion'),
    ]

    operations = [
        migrations.CreateModel(
            name='Pedido',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateField()),
                ('hora', models.TimeField()),
                ('cantidad', models.IntegerField()),
                ('fecha_ingreso', models.DateTimeField(auto_now_add=True)),
                ('fecha_actualizacion', models.DateTimeField(auto_now=True)),
                ('producto', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='Inventario.Inventario')),
                ('usuario', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='Usuario.Usuario')),
            ],
        ),
    ]
