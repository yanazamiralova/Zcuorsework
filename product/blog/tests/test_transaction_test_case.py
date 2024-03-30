from unittest import skip
from django.test import TransactionTestCase
from blog.models import Goog



class WidgetTransactionTestCase(TransactionTestCase):
    def test_widget_creation(self):
        Goog.objects.create(title='Шоколадный торт', price=100)
        Goog.objects.create(title='Молоко', price=120)
        self.assertEqual(Goog.objects.count(), 2)