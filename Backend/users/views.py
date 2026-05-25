from django.shortcuts import render
# Agrega estas dos líneas indispensables para Django REST Framework:
from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view(['GET'])
def products(request):
    # 'select_related' hace un JOIN en la base de datos para traer la categoría de un solo golpe (Evita lentitud)
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
    # Mantenemos el cálculo directo ya que es un JSON estadístico plano muy eficiente
    data = {
        "total_categories": Category.objects.count(),
        "total_products": Product.objects.count(),
        "low_stock_products": Product.objects.filter(stock__lte=5).count()
    }
    return Response(data)

@api_view(['GET'])
def payments(request):
    queryset = Payments.objects.all()
    serializer = PaymentsSerializer(queryset, many=True)
    return Response(serializer.data)
