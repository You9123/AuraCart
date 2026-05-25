from rest_framework import serializers
from .models import Category, Product, Payments

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name']

class ProductSerializer(serializers.ModelSerializer):
    # Trae el nombre de la categoría automáticamente sin bucles manuales
    category_name = serializers.CharField(source='category.name', read_only=True)

    class Meta:
        model = Product
        fields = ['id', 'name', 'price', 'stock', 'created_at', 'category', 'category_name']

class PaymentsSerializer(serializers.ModelSerializer):
    # Campo personalizado para ocultar el CVV en el JSON de salida
    cvv_hidden = serializers.SerializerMethodField()

    class Meta:
        model = Payments
        fields = ['id', 'user', 'cardType', 'cardNumber', 'expirationDate', 'cvv_hidden']

    def get_cvv_hidden(self, obj):
        # Retorna asteriscos según la longitud del CVV real (3 o 4 dígitos)
        return "*" * len(obj.cvv) if obj.cvv else ""
