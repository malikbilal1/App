from django.test import TestCase
from api.calc import addition

class CalcTests(TestCase):
    def test_add_numbers(self):
        self.assertEqual(addition(4,6), 10)