from django.urls import path
from .views import InventoryView

# urls here

urlpatterns = [
    path('inventory/', InventoryView.as_view())
]