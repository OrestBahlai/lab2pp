from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=250)

    def __str__(self):
        return str(self.name)


class Product(models.Model):
    name = models.CharField(max_length=250)
    status = models.CharField(max_length=250)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.name)


class User(models.Model):
    username = models.CharField(unique=True, max_length=250)
    firstname = models.CharField(max_length=250)
    lastname = models.CharField(max_length=250)
    password = models.CharField(max_length=250)
    user_status = models.IntegerField()

    def __str__(self):
        return str(self.username)


class Customer(models.Model):
    email = models.CharField(max_length=250)
    phone = models.CharField(max_length=250)
    username = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.username)


class Order(models.Model):
    quantity = models.IntegerField()
    status = models.CharField(max_length=250)
    shipDate = models.DateTimeField()
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    products = models.ManyToManyField(Product)

    def __str__(self):
        return str(self.customer) + ' ' + str(self.shipDate)

