from django.test import TestCase
from api.calc import addition

class CalcTest(TestCase):
    def test_add_numbers(self):
        self.assertEqual(addition(4,6), 10)