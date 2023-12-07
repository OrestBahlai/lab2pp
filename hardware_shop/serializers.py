from rest_framework import serializers
from hardware_shop.models import Product, User, Order


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('productId', 'name', 'status', 'category')


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('userId', 'username', 'firstname', 'lastname', 'email', 'phone', 'address')


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ('orderId', 'quantity', 'status', 'shipDate', 'user', 'products')

