from django.urls import path
from .views import(
    categories,
    products,
)

urlpatterns = [
   path('categories/', categories),
   path('products/', products),
]