import unittest
from tax import calc_tax


class TestCalcTax(unittest.TestCase):

    def test_calc_tax_with_incorrect_age_type_should_raise_error(self):
        self.assertRaises(TypeError, calc_tax, 60000, 0.15, '25')

    def test_calc_tax_with_negative_age_should_raise_error(self):
        self.assertRaises(ValueError, calc_tax, 60000, 0.23, -1)

    def test_calc_tax_equal_under_eighteen(self):
        self.assertAlmostEqual(calc_tax(60000, 0.2, 15), 5000)

    def test_calc_tax_equal_under_sixty_six(self):
        self.assertAlmostEqual(calc_tax(100000, 0.2, 32), 20000)

    def test_calc_tax_equal_above_sixty_six(self):
        self.assertAlmostEqual(calc_tax(70000, 0.2, 66), 8000)
