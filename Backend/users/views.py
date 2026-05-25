from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Category, Product
from .serializers import CategorySerializer, ProductSerializer, PaymentsSerializer
from django.shortcuts import render
from django.http import JsonResponse
from .models import Category, Product, Payments


@api_view(['GET'])
def products(request):
    # select_related optimiza la base de datos para traer las categorías de un solo golpe
    queryset = Product.objects.select_related('category').all()
    serializer = ProductSerializer(queryset, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def categories(request):
    queryset = Category.objects.all()
    serializer = CategorySerializer(queryset, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def dashboard_stats(request):
    # Esta estadística se puede quedar calculada directamente ya que devuelve un JSON plano
    data = {
        "total_categories": Category.objects.count(),
        "total_products": Product.objects.count(),
        "low_stock_products": Product.objects.filter(stock__lte=5).count()
    }
    return Response(data)
    return JsonResponse(data)


@api_view(['GET'])
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
