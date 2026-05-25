from django.contrib import admin

# Register your models here.

from django.contrib import admin
from .models import Category, Product, Payments


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')  # Muestra el ID y el Nombre en columnas
    search_fields = ('name',)     # Añade una barra de búsqueda por nombre


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    # Añadí 'stock' y 'created_at' para que aproveches las columnas de tu modelo
    list_display = ('id', 'name', 'price', 'stock', 'category', 'created_at')
    search_fields = ('name',)
    list_filter = ('category', 'created_at')


@admin.register(Payments)
class PaymentsAdmin(admin.ModelAdmin):

    list_display = (
        'id',
        'user',
        'cardType',
        'cardNumber',
        'expirationDate',
        'masked_cvv',
        'created_at'
    )

    search_fields = (
        'user',
        'cardType'
    )

    list_filter = (
        'cardType',
        'created_at'
    )

    def masked_cvv(self, obj):
        return "*" * len(obj.cvv)
