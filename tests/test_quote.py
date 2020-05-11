import unittest
from app.models import Quote

def setUp(self):
    self.new_quote = Quote(2,"Yoda","Do or do not there is no try")

def test_insistance(self):
    self.assertTrue(isinstance(self.new_quote,Quote))