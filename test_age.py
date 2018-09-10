from unittest import TestCase
from age import calculate_age

class Test(TestCase):
    def test_age(self):
        self.assertEquals(calculate_age(18),"You are a minor", "You are a youth")
        self.assertEquals(calculate_age(-1),"You are a minor", "Your age cannot be negative")
        self.assertEquals(calculate_age(20),"You are an elder", "You are a youth")
        self.assertEquals(calculate_age(10),"You are a youth", "You are a minor")




        