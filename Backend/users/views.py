from django.http import JsonResponse
from .models import (
    Category,
    Product,
)

def products(request):
    data = []
    # Traemos todos los productos
    for product in Product.objects.all():
        data.append({
            "id": product.id,
            "name": product.name,
            "price": product.price,
            "description": product.description,
            # Evaluamos: si tiene categoría asignada, extrae el nombre; si no, avisa que está vacío
            "category": product.category.name if product.category else "No category assigned in DB"
        })
        
    return JsonResponse(data, safe=False)

def categories(request):
    data = []
    # Traemos todas las categorías
    for category in Category.objects.all():
        data.append({
            "id": category.id,
            "name": category.name,
        })
        
    return JsonResponse(data, safe=False)  


