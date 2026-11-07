import random
import unittest


def setUpModule():
    print('In setUpModule()')


def tearDownModule():
    print('In tearDownModule()')


class FixturesTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print('In setUpClass()')
        cls.good_range = range(1, 10)
        print(type(cls.good_range))

    @classmethod
    def tearDownClass(cls):
        print('In tearDownClass()')
        del cls.good_range

    def setUp(self):
        super().setUp()
        print('\nIn setUp()')
        self.value = random.randint(
            self.good_range.start,
            self.good_range.stop - 1,
        )
        print(self.value)

    def tearDown(self):
        print('In tearDown()')
        del self.value
        super().tearDown()

    def test1(self):
        print('In test1()')
        self.assertIn(self.value, self.good_range)

    def test2(self):
        print('In test2()')
        self.assertIn(self.value, self.good_range)

if __name__ == '__main__':
    unittest.main()