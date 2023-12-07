from django.contrib import admin
from .models import User, Customer, Category, Product, Order

admin.site.register(Customer)

admin.site.register(User)

admin.site.register(Category)

admin.site.register(Product)

admin.site.register(Order)

