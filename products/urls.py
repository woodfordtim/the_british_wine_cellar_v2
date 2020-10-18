from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_wines, name='products'),
    path('<product_id>', views.product_detail, name='product_detail'),
]