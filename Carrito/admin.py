from django.contrib import admin
from .models import  Catalogo

@admin.register(Catalogo)
class CatalogoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'precio', 'imagen')
    search_fields = ('nombre',)
