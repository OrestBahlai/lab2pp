from django.urls import path
from hardware_shop.views import productApi, userApi

urlpatterns = [
    path('product/<int:productId>', productApi, name='product_detail'),
    path('user/<int:userId>', userApi, name='user_detail')
]
