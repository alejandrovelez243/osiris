from django.contrib import admin
from .models import Inventario
# Register your models here.


@admin.register(Inventario)
class InventarioAdmin(admin.ModelAdmin):
    list_display = ('producto', 'cantidad', 'valor_compra', 'valor_venta', 'ganancia')
