from django.test import TestCase
from hardware_shop.models import Product

class ProductTestCase(TestCase):
    def setUp(self):
        Product.objects.create(productId=100, name='Sniezka Eko 20L', status='sold', category='Paintings')

    def test_product(self):
        product = Product.objects.get(productId=100)
        self.assertEqual(product.name,'Sniezka Eko 20L')
        self.assertEqual(product.status, 'sold')

