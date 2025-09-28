from django.urls import path
from . import views

urlpatterns = [
    path('', views.proyecto_lista, name='proyecto_lista'),
    path('new/', views.proyecto_crear, name='proyecto_crear'),
    path('<int:pk>/', views.proyecto_detalle, name='proyecto_detalle'),
]
