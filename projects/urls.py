# projects/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('crear/', views.crear_proyecto, name='crear_proyecto'),  # para crear un proyecto
    path('', views.lista_proyectos, name='lista_proyectos'),      # lista todos los proyectos
    path('<int:pk>/', views.detalle_proyecto, name='detalle_proyecto'),  # detalles de un proyecto
]
