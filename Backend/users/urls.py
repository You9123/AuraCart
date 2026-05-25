from django.urls import path
from .views import(
    categories,
    products,
)

urlpatterns = [
   path('categories/', categories, name='categories'),
   path('products/', products, name='products'),
]