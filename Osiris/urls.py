from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    path('', include('myapps.Dashboard.urls')),
    path('usuarios', include('myapps.Usuario.urls')),
    path('productos', include('myapps.Productos.urls')),
    path('Pedido', include('myapps.Pedido.urls')),
    path('Inventario', include('myapps.Inventario.urls')),
    path('Informes', include('myapps.Informe.urls')),
    path('Empresa', include('myapps.Empresa.urls')),
]