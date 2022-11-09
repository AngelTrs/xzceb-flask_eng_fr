import unittest
from translator import englishToFrench, frenchToEnglish

class TestEnglishToFrench(unittest.TestCase):
    def test1(self): 
        self.assertEqual(englishToFrench("55"), "55")
    def test2(self): 
        self.assertNotEqual(englishToFrench("Oui"), "Yes") 
    def test3(self): 
        self.assertIsNone(englishToFrench(None), "Input is null.")
    def test4(self): 
        self.assertEqual(englishToFrench("Hello"), "Bonjour")

class TestFrenchtoEnglish(unittest.TestCase): 
    def test1(self): 
        self.assertEqual(frenchToEnglish("55"), "55")
    def test2(self): 
        self.assertNotEqual(frenchToEnglish("Yes"), "Qui") 
    def test3(self): 
        self.assertIsNone(frenchToEnglish(None), "Input is null.")
    def test4(self): 
        self.assertEqual(frenchToEnglish("Bonjour"), "Hello")

unittest.main()