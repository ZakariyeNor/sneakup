from django.urls import path
from . import views

# Urls

urlpatterns = [
    path('', views.privacy_policy, name='privacy_policy'),
]