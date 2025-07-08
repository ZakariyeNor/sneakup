from django.urls import path
from . import views

# Urls for checkout views
urlpatterns = [
    path('', views.checkout, name='checkout'),
]