from django.urls import path
from . import views


urlpatterns = [
    path('', views.proyecto_lista, name='proyecto_lista'),
    path('new/', views.proyecto_crear, name='proyecto_crear'),
    path('<int:pk>/', views.proyecto_detalle, name='proyecto_detalle'),
    path('<int:pk>/eliminar/', views.proyecto_eliminar, name='proyecto_eliminar'),
    path('<int:pk>/editar/', views.proyecto_editar, name='proyecto_editar'),
    path('archivo/<int:pk>/eliminar/', views.archivo_eliminar, name='archivo_eliminar'),

]
