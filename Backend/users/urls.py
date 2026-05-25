from django.urls import path
from .views import(
    categories,
    products,
    dashboard_stats
)

urlpatterns = [
   path('categories/', categories),
   path('products/', products),
   path('dashboard_stats/',dashboard_stats),
]