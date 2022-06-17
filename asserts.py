# #assertTrue
# import unittest
# from selenium import webdriver
# class test_case1(unittest.TestCase):
#     def test1(self):
#         s1 ="Python"
#         s2 ="Ruby"
#         # Verifying Numbers
#         self.assertTrue(s1== s2, "It's not a Match.")

# unittest.main()

#assertFalse
import unittest
from selenium import webdriver
class test_case1(unittest.TestCase):
    def test1(self):
        s1 ="Python"
        s2 ="Ruby"
        # Verifying Numbers
        self.assertFalse(s1== s2, "It's not a Match.")
        
    def test2(self):
        s1 ="Python"
        # Verifying Numbers
        self.assertFalse(s1 == 'Ruby', "it's a match.")
unittest.main()