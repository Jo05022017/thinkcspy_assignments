from .solution import hello
import unittest

class TestChapter05(unittest.TestCase):

    def test_solution(self):
    	self.assertEqual(hello(), "Hello world") # this should succeed

    		
    	
