from django.test import TestCase
from api.calc import adda

class CalcTests(TestCase):
    def test_add_numbers(self):
        self.assertEqual(adda(4,6), 10)