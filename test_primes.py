import unittest
from primes import is_prime

class PrimesTestCase(unittest.TestCase):
    """Test primes.py."""

    def test_is_five_prime(self):
        self.assertTrue(is_prime(5))

    def test_is_four_non_prime(self):
        self.assertFalse(is_prime(4), msg='Four is not prime!')

    def test_is_zero_not_prime(self):
        self.assertFalse(is_prime(0))

    def test_is_one_not_prime(self):
        self.assertFalse(is_prime(1))

    def test_negative_number(self):
        """Is a negative number correctly determined not to be prime?"""
        for index in range(-1, -10, -1):
            self.assertFalse(is_prime(index), msg='{} should not be determined to be prime'.format(index))

if __name__ == '__main__':
    unittest.main()