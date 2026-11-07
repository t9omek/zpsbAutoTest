import unittest

class FirstTest(unittest.TestCase):
    def testA(self):
        """Test A"""
        print("FirstTest: test A")

    def testB(self):
        """Test A"""
        print("FirstTest: test B")

class SecondTest(unittest.TestCase):
    def testC(self):
        """Test C"""
        print("SecondTest: test C")

    def testD(self):
        """Test D"""
        print("SecondTest: testD")

class ThirdTest(unittest.TestCase):
    def testE(self):
        """Test E"""
        print("ThirdTest: testE")


loader = unittest.TestLoader()
suite  = unittest.TestSuite()

suite.addTests(loader.loadTestsFromTestCase(FirstTest))
suite.addTests(loader.loadTestsFromTestCase(SecondTest))
suite.addTests(loader.loadTestsFromTestCase(ThirdTest))

if __name__ == '__main__':
    runner = unittest.TextTestRunner(verbosity=1)
    result = runner.run(suite)
