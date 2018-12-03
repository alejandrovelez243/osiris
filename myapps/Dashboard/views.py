from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from myapps.Usuario.models import Usuario

# Create your views here.

@login_required
def index(request):
    usuario = Usuario.objects.get(usuario = request.user.id)
    data = {
        'nombre':usuario.usuario.first_name + " " + usuario.usuario.last_name
    }
    return render(request, 'Dashboard/index.html', data)