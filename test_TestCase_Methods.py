import unittest


class BuildInMethodsTest(unittest.TestCase):

    # przygotowanie testcasa
    def setUp(self):
        """ Setting up for the test """
        print("BuildInMethodsTest:setUp_:begin")
        # actions
        print("BuildInMethodsTest:setUp_:end")

    # zakończenie testcasa
    def tearDown(self):
        """Cleaning up after the test"""
        print("BuildInMethodsTest:tearDown_:begin")
        # actions
        print("BuildInMethodsTest:tearDown_:end")

    # przebiek testu A
    def testA(self):
        """Test A"""
        print("BuildInMethodsTest:testA")
        print(self.shortDescription())

    # przebieg testu B
    def testB(self):
        """Test B"""
        print("BuildInMethodsTest:testB")
        print(self.shortDescription())

if __name__ == '__main__':
    unittest.main()