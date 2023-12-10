from django.test import TestCase
from hardware_shop.models import Product, User


class ProductTestCase(TestCase):
    def setUp(self):
        Product.objects.create(productId=100, name='Sniezka Eko 20L', status='sold', category='Paintings')

    def test_product(self):
        product = Product.objects.get(productId=100)
        self.assertEqual(product.name, 'Sniezka Eko 20L')
        self.assertEqual(product.status, 'sold')

    def test_product_category(self):
        product = Product.objects.get(productId=100)
        self.assertEqual(product.category, 'Paintings')

    def test_product_update(self):
        product = Product.objects.get(productId=100)
        product.name = 'New Product'
        product.save()
        updated_product = Product.objects.get(productId=100)
        self.assertEqual(updated_product.name, 'New Product')

    def test_product_delete(self):
        product = Product.objects.get(productId=100)
        product.delete()
        with self.assertRaises(Product.DoesNotExist):
            deleted_product = Product.objects.get(productId=100)


class UserTestCase(TestCase):
    def setUp(self):
        User.objects.create(userId=27, username='theUser', firstname='Petro', lastname='Lysak', email='petro.lysak@email.com', phone='12345', address='Lviv, Zelena 45/8, 79005')

    def test_user(self):
        user = User.objects.get(userId=27)
        self.assertEqual(user.username, 'theUser')
        self.assertEqual(user.phone, '12345')

    def test_user_firstname(self):
        user = User.objects.get(userId=27)
        self.assertEqual(user.firstname, 'Petro')

    def test_user_lastname(self):
        user = User.objects.get(userId=27)
        self.assertEqual(user.lastname, 'Lysak')

    def test_user_email(self):
        user = User.objects.get(userId=27)
        self.assertEqual(user.email, 'petro.lysak@email.com')

    def test_user_address(self):
        user = User.objects.get(userId=27)
        self.assertEqual(user.address, 'Lviv, Zelena 45/8, 79005')

    def test_user_update(self):
        user = User.objects.get(userId=27)
        user.username = 'NewUser'
        user.save()
        updated_user = User.objects.get(userId=27)
        self.assertEqual(updated_user.username, 'NewUser')

    def test_user_delete(self):
        user = User.objects.get(userId=27)
        user.delete()
        with self.assertRaises(User.DoesNotExist):
            deleted_user = User.objects.get(userId=27)



