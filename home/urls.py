from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('email_subscribe/', views.email_subscribe, name='email_subscribe'),
]
