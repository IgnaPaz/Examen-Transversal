from django.urls import path
from . import views  
from django.urls import path, include


urlpatterns = [
    path('', views.catalogo_list, name='listar_catalogo'),
    path('create', views.catalogo_create, name='crear_catalogo'),
    path('edit/<int:pk>/', views.catalogo_update, name='modificar_catalogo'),
    path('delete/<int:pk>/', views.catalogo_delete, name='eliminar_catalogo'),
    path('iniciar/', views.iniciar_sesion, name='iniciar'),
    path('inicio/', views.index, name='index'),
    path('registrar/', views.registrar, name='registrar'),
    path('carrito/', views.carrito_view, name='carrito'),  
    path('empleados/', views.empleados, name='empleados'),
    path('novias/', views.novias, name='novias'),
    path('novios/', views.novios, name='novios'),
    # path('carrito/', include('carrito.urls'))
    path('nueva_iniciar/', views.nueva_iniciar_sesion, name='nueva_iniciar_sesion'),
    path
]
