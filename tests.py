import unittest
from contrived_func import contrived_func


class TestContrivedFunc(unittest.TestCase):
    def test_case_0(self):  # a=T, b=F, c=F, d=T
        contrived_func(0)

    def test_case_1(self):  # a=T, b=T, c=F, d=T
        contrived_func(1)

    def test_case_2(self):  # a=T, b=F, c=F, d=F
        contrived_func(3)

    def test_case_3(self):  # a=T, b=F, c=F, d=F - perhaps remove?
        contrived_func(6)

    def test_case_4(self):  # a=F, b=T, c=F, d=F
        contrived_func(20)

    def test_case_5(self):  # a=F, b=T, c=T, d=F
        contrived_func(45)

    def test_case_6(self):  # a=F, b=F, c=T, d=T
        contrived_func(-20)


if __name__ == "__main__":
    unittest.main()