import unittest
from unitcalc.value_types.value import CustomValue


class CustomValueEquals(unittest.TestCase):

    def test_equals_same_units(self):
        self.assertTrue(CustomValue(2.34,kg=1,A=-1) == CustomValue(2.34,kg=1,A=-1))

    def test_equals_same_units_diff_values(self):
        self.assertFalse(CustomValue(4.32,kg=1,A=-1) == CustomValue(2.34,kg=1,A=-1))

    def test_equals_diff_units(self):
        self.assertFalse(CustomValue(2.34,kg=1,A=-1) == CustomValue(2.34,kg=-1,A=1))


    def test_equals_dimless_and_int(self):
        self.assertTrue(CustomValue(2) == 2)

    def test_equals_dimless_and_int_diff_values(self):
        self.assertFalse(CustomValue(2) == 3)

    def test_equals_dimless_and_float(self):
        self.assertTrue(CustomValue(1.23) == 1.23)

    def test_equals_dimless_and_float_diff_values(self):
        self.assertFalse(CustomValue(1.23) == 3.21)

    def test_equals_differrent_object(self):
        self.assertFalse(CustomValue(2.34,kg=1,A=-1) == "str-type")


class CustomValueNotEquals(unittest.TestCase):

    def test_not_equals_same_units(self):
        self.assertFalse(CustomValue(2.34,kg=1,A=-1) != CustomValue(2.34,kg=1,A=-1))

    def test_not_equals_same_units_diff_values(self):
        self.assertTrue(CustomValue(4.32,kg=1,A=-1) != CustomValue(2.34,kg=1,A=-1))

    def test_not_equals_diff_units(self):
        self.assertTrue(CustomValue(2.34,kg=1,A=-1) != CustomValue(2.34,kg=-1,A=1))


    def test_not_equals_dimless_and_int(self):
        self.assertFalse(CustomValue(2) != 2)

    def test_not_equals_dimless_and_int_diff_values(self):
        self.assertTrue(CustomValue(2) !=3)

    def test_not_equals_dimless_and_float(self):
        self.assertFalse(CustomValue(1.23) !=1.23)

    def test_not_equals_dimless_and_float_diff_values(self):
        self.assertTrue(CustomValue(1.23) != 3.21)

    def test_not_equals_differrent_object(self):
        self.assertTrue(CustomValue(2.34,kg=1,A=-1) != "str-type")
