from django.urls import path
from .views import products

add_name = 'mainapp'

urlpatterns = [
    path('', products, name='products'),
]