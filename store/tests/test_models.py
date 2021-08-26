from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse

from store.models import Category, Product


class TestCategoriesModel(TestCase):

    def setUp(self):
        self.data1 = Category.objects.create(name='ropes', slug='ropes')

    def test_category_model_entry(self):
        """
        Test category model data insertion/types/field attributes
        """
        data = self.data1
        self.assertTrue(isinstance(data, Category))

    def test_category_model_url(self):
        """
        Test Category model default name
        """
        data = self.data1
        response = self.client.post(
            reverse('store:category_list', args=[data.slug])
        )
        self.assertEqual(response.status_code, 200)


class TestProductsModel(TestCase):
    def setUp(self):
        Category.objects.create(name='foster', slug='ropes')
        User.objects.create(username='foster')
        self.data1 = Product.objects.create(category_id=1,
                                            title='django beginners',
                                            created_by_id=1,
                                            slug='django-beginners',
                                            price='16.16', image='django')

    def test_products_model_entry(self):
        """
        Test product model slug and URL reverse
        """
        data = self.data1
        self.assertTrue(isinstance(data, Product))
        self.assertEqual(str(data), 'django beginners')

    def test_products_custom_manager_basic(self):
        """
        Test product model custom manager
        returns only active products
        """
        data = Product.objects.all()
        self.assertEqual(data.count(), 1)
