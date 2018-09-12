from unittest import TestCase
from age import calculate_age

class Test(TestCase):
    def test_age(self):
        self.assertEqual(calculate_age(2000), "You are a youth")
        self.assertEqual(calculate_age(2019), "Your age cannot be negative")
        self.assertEqual(calculate_age(1995), "You are a youth")
        self.assertEqual(calculate_age(2005),"You are a minor")




        