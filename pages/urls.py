from django.urls import path
from . import views

# Urls

urlpatterns = [
    path('privacy_policy/', views.privacy_policy, name='privacy_policy'),
    path('returns_policy/', views.returns_policy, name='returns_policy'),
    path('faqs/', views.faqs_view, name='faqs_view'),
    path('contact/', views.contact, name='contact'),
    path('about_us/', views.about_view, name='about_view'),
]
