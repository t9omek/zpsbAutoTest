import unittest


def raises_error(*args, **kwds):
    raise ValueError('Invalid value: ' + str(args) + str(kwds))


class ExceptionTest(unittest.TestCase):

    def testTrapLocally(self):
        try:
            raises_error('a', b='c')
        except ValueError:
            pass
        else:
            self.fail('ValueError was not raised')

    def testAssertRaises(self):
        self.assertRaises(ValueError, raises_error, 'a', b='c')

if __name__ == '__main__':
    unittest.main()
