from django.db import models


class Product(models.Model):
    productId = models.AutoField(primary_key=True)
    name = models.CharField(max_length=250)
    status = models.CharField(max_length=250)
    category = models.CharField(max_length=250)

    def __str__(self):
        return str(self.productId) + ', ' + str(self.name) + ', ' + str(self.status)


class User(models.Model):
    userId = models.AutoField(primary_key=True)
    username = models.CharField(unique=True, max_length=250)
    firstname = models.CharField(max_length=250)
    lastname = models.CharField(max_length=250)
    email = models.CharField(max_length=250)
    phone = models.CharField(max_length=250)
    address = models.CharField(max_length=250)

    def __str__(self):
        return str(self.userId) + ', ' + str(self.username)


class Order(models.Model):
    orderId = models.AutoField(primary_key=True)
    quantity = models.IntegerField()
    status = models.CharField(max_length=250)
    shipDate = models.DateTimeField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    products = models.ManyToManyField(Product)

    def __str__(self):
        return str(self.orderId) + ' ' + str(self.user) + ' ' + str(self.shipDate)

