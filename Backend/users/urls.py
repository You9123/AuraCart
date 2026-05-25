from django.urls import path
from .views import (
    categories,
    products,
    payments,
    dashboard_stats
)

urlpatterns = [
    path('categories/', categories),
    path('products/', products),
    path('dashboard_stats/', dashboard_stats),
    path('payments/', payments),
]
