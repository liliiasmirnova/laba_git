import unittest
from calc import add, sub, mul, div


class TestCalc(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(2, 3), 5)

    def test_sub(self):
        self.assertEqual(sub(5, 3), 2)

    def test_mul(self):
        self.assertEqual(mul(2, 4), 8)

    def test_div(self):
        self.assertEqual(div(8, 2), 4)
        self.assertIsNone(div(1, 0))


if __name__ == "__main__":
    unittest.main()
