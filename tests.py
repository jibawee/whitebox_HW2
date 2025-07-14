import unittest
from contrived_func import contrived_func

class TestContrivedFunc(unittest.TestCase):

    def test_case_0(self):
        contrived_func(0)

    def test_case_1(self):
        contrived_func(1)

    def test_case_minus_1(self):
        contrived_func(-1)

    def test_case_100(self):
        contrived_func(100)

    def test_case_double(self):
        contrived_func(1.5)

if __name__ == '__main__':
    unittest.main()
