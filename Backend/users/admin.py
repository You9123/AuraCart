from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Category, Product, Payments, CustomUser


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


@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):

    list_display = (
        'id',
        'username',
        'email',
        'first_name',
        'last_name',
        'role',
        'is_staff',
        'is_superuser'
    )

    list_filter = (
        'role',
        'is_staff',
        'is_superuser'
    )

    fieldsets = UserAdmin.fieldsets + (

        ('AuraCart Extra Info', {
            'fields': (
                'address',
                'birth_date',
                'role',
            )
        }),
    )

    add_fieldsets = UserAdmin.add_fieldsets + (

        ('AuraCart Extra Info', {
            'fields': (
                'first_name',
                'last_name',
                'email',
                'address',
                'birth_date',
                'role',
            )
        }),
    )
