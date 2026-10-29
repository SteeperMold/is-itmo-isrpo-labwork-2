import math
import unittest

from circle import area, perimeter


class CircleTestCase(unittest.TestCase):
    def test_area_unit_radius(self):
        self.assertAlmostEqual(area(1), math.pi)

    def test_perimeter_unit_radius(self):
        self.assertAlmostEqual(perimeter(1), 2 * math.pi)

    def test_area_radius_two(self):
        self.assertAlmostEqual(area(2), 4 * math.pi)

    def test_perimeter_radius_two(self):
        self.assertAlmostEqual(perimeter(2), 4 * math.pi)

    def test_zero_radius(self):
        self.assertEqual(area(0), 0)
        self.assertEqual(perimeter(0), 0)

    def test_negative_radius_area(self):
        with self.assertRaises(ValueError):
            area(-2)

    def test_negative_radius_perimeter(self):
        with self.assertRaises(ValueError):
            perimeter(-2)

    def test_string_radius(self):
        with self.assertRaises(TypeError):
            area("abc")


if __name__ == "__main__":
    unittest.main()
