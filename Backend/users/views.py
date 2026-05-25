from django.shortcuts import render
from django.http import JsonResponse
from .models import Category, Product, Payments


def products(request):
    data = []
    # Traemos todos los productos de tu modelo real
    for product in Product.objects.all():
        data.append({
            "id": product.id,
            "name": product.name,
            # Lo pasamos a string para que no de problemas con decimales en JS
            "price": str(product.price),
            "stock": product.stock,        # ¡Añadido para el Front!
            # ¡Añadido para el Front!
            "created_at": product.created_at.isoformat() if product.created_at else None,
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


def payments(request):
    data = []

    for payment in Payments.object.all():

        data.append({

            "id": payment.id,

            "user": payment.user,

            "cardType": payment.cardType,

            "cardNumber": payment.cardNumber,

            "expirationDate": payment.expirationDate,

            # CVV Oculto
            "cvv": "*" * len(payment.cvv),

            "created_at": payment.created_at.isoformat()
            if payment.created_at else None
        })
    return JsonResponse(data, safe=False)
