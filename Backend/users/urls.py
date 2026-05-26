from django.urls import path
from .views import (
    categories,
    products,
    payments,
    users,
    dashboard_stats
)

urlpatterns = [
    path('categories/', categories),
    path('products/', products),
    path('payments/', payments),
    path('users/', users),
    path('dashboard_stats/', dashboard_stats),
]
