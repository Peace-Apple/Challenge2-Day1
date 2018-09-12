from unittest import TestCase
from square_dictionary import dictionary

class Test(TestCase):
    def test_dictionary(self):
        self.assertEqual(dictionary(2,3),{2:4})
        self.assertEqual(dictionary(3,4),{3:9})
       


