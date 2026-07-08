from django.urls import path
from . import views  # Usa o ponto (.) para referenciar a pasta atual

urlpatterns = [
    path('', views.index, name='index'),
]
