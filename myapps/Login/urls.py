from django.urls import path, include
from django.contrib.auth.decorators import login_required
from .views import index

urlpatterns = [
    path('', login_required(index), name='index'),
]
