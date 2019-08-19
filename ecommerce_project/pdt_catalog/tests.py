from django.test import TestCase

from .models import Seller, Category, Product


# Create your tests here.
class SellerModelTests(TestCase):
    def test_seller_creation(self):
        seller = Seller.objects.create(
            name='Seller 1',
            description="This is the first seller",
        )

        self.assertEqual('Seller 1', seller.name)


class SellerViewTests(TestCase):
    def setUp(self):
        self.seller1 = Seller.objects.create(
            name='Seller 1',
            description="first seller",
        )
        self.seller2 = Seller.objects.create(
            name='Seller 2',
            description="Second seller",
        )
