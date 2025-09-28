# portal_proyectos/urls.py
from django.contrib import admin
from django.urls import path, include  # include es necesario para enlazar urls de apps

urlpatterns = [
    path('admin/', admin.site.urls),
    path('projects/', include('projects.urls')),  # enlaza todas las URLs de la app projects
]
