from django.urls import path
from . import views
from .webhooks import webhook

# Urls for checkout views
urlpatterns = [
    path('', views.checkout, name='checkout'),
    path('checkout_success/<str:order_number>/', views.checkout_success, name='checkout_success'),
    path('webhook/', webhook, name='webhook'),
]