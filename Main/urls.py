"""
URL configuration for Main project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from Carrito import views


urlpatterns = [
    path('admin/', admin.site.urls),
    # path('carrito/', include('carrito.urls')),
    # path('', include('Carrito.urls')),
    path('',views.index, name='index'),
     path('carrito/', views.carrito_view, name='carrito'),  
    path('empleados/', views.empleados, name='empleados'),
    path('novias/', views.novias, name='novias'),
    path('novios/', views.novios, name='novios'),
     path('iniciar/', views.iniciar_sesion, name='iniciar'),
    path('registrar/', views.registrar, name='registrar'),
    path('', views.catalogo_list, name='listar_catalogo'),
    path('create', views.catalogo_create, name='crear_catalogo'),
     path('edit/<int:pk>/', views.catalogo_update, name='modificar_catalogo'),
     path('delete/<int:pk>/', views.catalogo_delete, name='eliminar_catalogo'),
    path('catalogo/<int:pk>/', views.detalle_catalogo, name='detalle_catalogo'),
     path('nueva_iniciar/', views.nueva_iniciar_sesion, name='nueva_iniciar_sesion'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)