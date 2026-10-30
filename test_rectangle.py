import unittest

from square import area, perimeter


class SquareTestCase(unittest.TestCase):
    def test_area(self):
        self.assertEqual(area(5), 25)

    def test_perimeter(self):
        self.assertEqual(perimeter(5), 20)

    def test_fractional_side(self):
        self.assertAlmostEqual(area(2.5), 6.25)
        self.assertAlmostEqual(perimeter(2.5), 10.0)

    def test_zero_side(self):
        self.assertEqual(area(0), 0)
        self.assertEqual(perimeter(0), 0)

    def test_negative_side_area(self):
        with self.assertRaises(ValueError):
            area(-5)

    def test_negative_side_perimeter(self):
        with self.assertRaises(ValueError):
            perimeter(-5)

    def test_string_side(self):
        with self.assertRaises(TypeError):
            area("abc")

    def test_complex_side_area(self):
        with self.assertRaises(TypeError):
            area(2 + 3j)

    def test_complex_side_perimeter(self):
        with self.assertRaises(TypeError):
            perimeter(2 + 3j)


if __name__ == "__main__":
    unittest.main()
