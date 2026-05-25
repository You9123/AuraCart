from django.shortcuts import render
from django.http import JsonResponse
from .models import Category, Product

def products(request):
    data = []
    # Traemos todos los productos de tu modelo real
    for product in Product.objects.all():
        data.append({
            "id": product.id,
            "name": product.name,
            "price": str(product.price),  # Lo pasamos a string para que no de problemas con decimales en JS
            "stock": product.stock,        # ¡Añadido para el Front!
            "created_at": product.created_at.isoformat() if product.created_at else None, # ¡Añadido para el Front!
            # Evaluamos la relación
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

def dashboard_stats(request):
    data = {
        "total_categories": Category.objects.count(),
        "total_products": Product.objects.count(),
        "low_stock_products": Product.objects.filter(stock__lte=5).count()
    }
    return JsonResponse(data)
