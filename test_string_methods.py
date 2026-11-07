import unittest

class TestStringMethods(unittest.TestCase):

    def test_upper(self):
        self.assertEqual('studenciak'.upper(), 'STUDENCIAK')

    def test_isupper(self):
        self.assertTrue('STUDENCIAK'.isupper())
        self.assertFalse('studenciak'.isupper())

    def test_split(self):
        s = 'hello studenciak'
        self.assertEqual(s.split(), ['hello', 'studenciak'])
        # check that s.split fails when the separator is not a string
        with self.assertRaises(TypeError):
            s.split(2)

if __name__ == '__main__':
    unittest.main()