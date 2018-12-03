from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from myapps.Usuario.models import Usuario

# Create your views here.

@login_required
def index(request):
    return render(request, 'Dashboard/index.html')