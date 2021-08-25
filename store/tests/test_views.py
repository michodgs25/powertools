from unittest import skip 

from django.test import TestCase
from django.contrib.auth.models import User

from store.models import Category, Product
from django.urls import reverse
from django.test import Client


#@skip("demonstrating skipping")
#class TestSkip(TestCase):
 #   def test_skip_example(self):
  #      pass


class TestViewResponses(TestCase):
    def setUp(self):
        self.c = Client()
        User.objects.create(username="foster")
        Category.objects.create(name='Ropes', slug='ropes')
        Product.objects.create(category_id=1, title='ropes', created_by_id=1,
                               slug='ropes', price='20.00', image='ropes')

        def test_url_allowed_hosts(self):
            """
            Test allowed hosts
            """
            response = self.c.get('/')
            self.assertEqual(response.status_code, 200)

        def test_product_detail_url(self):
            response = self.c.get(reverse('store:product_detail', args=['django']))
