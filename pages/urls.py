from django.urls import path
from . import views

# Urls

urlpatterns = [
    path('privacy_policy/', views.privacy_policy, name='privacy_policy'),
    path('returns_policy/', views.returns_policy, name='returns_policy'),
    path('faqs_view/', views.returns_policy, name='faqs_view'),
]