import unittest

from triangle import area, perimeter


class TriangleTestCase(unittest.TestCase):
    def test_area(self):
        self.assertEqual(area(6, 4), 12)

    def test_perimeter(self):
        self.assertEqual(perimeter(3, 4, 5), 12)

    def test_fractional_values(self):
        self.assertAlmostEqual(area(2.5, 3.5), 4.375)
        self.assertAlmostEqual(perimeter(2.5, 3.5, 4.5), 10.5)

    def test_zero_height(self):
        self.assertEqual(area(6, 0), 0)

    def test_zero_size(self):
        self.assertEqual(area(0, 6), 0)

    def test_negative_base_area(self):
        with self.assertRaises(ValueError):
            area(-6, 4)

    def test_negative_height_area(self):
        with self.assertRaises(ValueError):
            area(6, -4)

    def test_negative_side_perimeter(self):
        with self.assertRaises(ValueError):
            perimeter(3, -4, 5)

    def test_invalid_triangle(self):
        with self.assertRaises(ValueError):
            perimeter(1, 2, 10)

    def test_string_base(self):
        with self.assertRaises(TypeError):
            area("abc", 4)

    def test_complex_base_area(self):
        with self.assertRaises(TypeError):
            area(2 + 3j, 4)

    def test_complex_side_perimeter(self):
        with self.assertRaises(TypeError):
            perimeter(3, 2 + 3j, 5)


if __name__ == "__main__":
    unittest.main()
