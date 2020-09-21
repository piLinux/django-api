from django.test import TestCase
from app.calc import add, subtract


class CalcTests(TestCase):
    def test_add_numbers(self):
        """Unit test"""
        self.assertEqual(add(3, 8), 11)

    def test_subtract_numbers(self):
        """TDD: subtract values"""
        self.assertEqual(subtract(14, 8), 6)
