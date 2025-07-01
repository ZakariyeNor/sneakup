from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_products_view, name='products'),
    path('product_detail/<int:product_id>/', views.product_detail, name='product_detail'),
]