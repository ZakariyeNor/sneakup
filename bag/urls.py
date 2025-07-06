from django.urls import path
from . import views

urlpatterns = [
    path('bag/', views.view_bag, name='bag'),
    path('add/<int:item_id>/', views.add_to_bag, name='add_to_bag'),
    path('bag/update/<item_id>/', views.update_bag, name='update_bag'),
]
