from django.test import TestCase
from api.calc import add

class CalcTests(TestCase):
    def test_add_numbers(self):
        self.assertEqual(add(4,6), 10)