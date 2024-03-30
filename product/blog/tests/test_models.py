from unittest import skip
from django.test import TestCase
from blog.models import Goog


class MyModelTest(TestCase):
    def setUp(self):
        self.object = Goog.objects.create(title="Чай", price=100)

    def test_str_representation(self):
        self.assertEqual(str(self.object), 'Чай')

    def tearDown(self):
        pass
