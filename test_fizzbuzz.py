
import unittest
from fizzbuzz import affiche

class TestFizzBuzz(unittest.TestCase):
    def test_affiche(self):
        self.assertEqual(affiche(100), "1 2 Fizz 4 Buzz ... 99 Buzz")

    def test_affiche_avec_parametres(self):
        self.assertEqual(affiche(15), "1 2 Fizz 4 Buzz 7 8 Fizz Buzz 11 Fizz 13 14 Frisbee ")

    def test_affiche_avec_deux_parametres(self):
        self.assertEqual(affiche(5,10), "Buzz Fizz 7 8 Buzz Fizz")

if __name__ == "__main__":
    unittest.main()
