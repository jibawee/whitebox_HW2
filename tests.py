import unittest
from contrived_func import contrived_func

class TestContrivedFunc(unittest.TestCase):

    def test_case_1(self):
        contrived_func(0)

    def test_case_2(self):
        contrived_func(1)

    def test_case_3(self):
        contrived_func(100)

    def test_case_4(self):
        contrived_func(1.5)

    def test_case_5(self):
        contrived_func(1.55)

if __name__ == '__main__':
    unittest.main()