from unittest import TestCase
import square_dictionary

class Test(TestCase):
    def test_dictionary(self):
        self.assertEquals(square_dictionary.dictionary(2,3),{2:4})
        self.assertEquals(square_dictionary.dictionary(3,4),{3:9})
        print("It excutes")


