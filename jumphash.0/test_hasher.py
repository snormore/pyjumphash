import pyximport; pyximport.install()
import unittest

class TestHasher(unittest.TestCase):

    def test_hash_10_buckets(self):
        self.assertEqual(jumphash(10, 42), 1)

    def test_hash_100_buckets(self):
        self.assertEqual(jumphash(100, 42), 1)


if __name__ == '__main__':
    unittest.main()
