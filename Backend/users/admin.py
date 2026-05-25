from django.contrib import admin

# Register your models here.

from django.contrib import admin
from .models import Category, Product

# Esta es la versión avanzada de admin.site.register(Specialty)
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name') # Muestra el ID y el Nombre en columnas
    search_fields = ('name',)     # Añade una barra de búsqueda por nombre

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'price', 'description', 'category')
    search_fields = ('name', 'description')
    list_filter = ('category',)