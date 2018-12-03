# Generated by Django 2.1.1 on 2018-10-08 21:19

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Usuario', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuario',
            name='empresa',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='Empresa.Empresa'),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='usuario',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
