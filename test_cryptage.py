import unittest
from cryptage import crypt, decrypt

class TestCrypt(unittest.TestCase):
    def test_crypt(self):
        self.assertEqual(crypt("abc"), "bcd")
    def test_crypt_avec_pas(self):
        self.assertEqual(crypt("abc", 1), "bcd")
    def test_decrypt(self):
        self.assertEqual(decrypt("bcd", 1), "abc")

if __name__ == "__main__":
    unittest.main()
