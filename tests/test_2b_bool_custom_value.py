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


class CustomValueLessThan(unittest.TestCase):
    def test_lt_same_units_true(self):
        self.assertTrue(CustomValue(1.23,kg=1,A=-1) < CustomValue(4.56,kg=1,A=-1))

    def test_lt_same_units_false(self):
        self.assertFalse(CustomValue(4.56,kg=1,A=-1) < CustomValue(1.23,kg=1,A=-1))

    def test_lt_same_units_eq_false(self):
        self.assertFalse(CustomValue(1.23,kg=1,A=-1) < CustomValue(1.23,kg=1,A=-1))

    def test_lt_dimless_and_int_true(self):
        self.assertTrue(CustomValue(1) < 2)

    def test_lt_dimless_and_int_false(self):
        self.assertFalse(CustomValue(2) < 1)

    def test_lt_dimless_and_int_eq_false(self):
        self.assertFalse(CustomValue(2) < 2)

    def test_lt_dimless_and_float_true(self):
        self.assertTrue(CustomValue(1.234) < 4.321)

    def test_lt_dimless_and_float_false(self):
        self.assertFalse(CustomValue(4.321) < 1.234)

    def test_lt_dimless_and_float_eq_false(self):
        self.assertFalse(CustomValue(4.321) < 4.321)

    def test_lt_invalid(self):
        with self.assertRaises(TypeError):
            CustomValue(4.321) < "invalid"


class CustomValueGreaterThanEqual(unittest.TestCase):
    def test_ge_same_units_false(self):
        self.assertFalse(CustomValue(1.23,kg=1,A=-1) >= CustomValue(4.56,kg=1,A=-1))

    def test_ge_same_units_true(self):
        self.assertTrue(CustomValue(4.56,kg=1,A=-1) >= CustomValue(1.23,kg=1,A=-1))

    def test_ge_same_units_eq_true(self):
        self.assertTrue(CustomValue(1.23,kg=1,A=-1) >= CustomValue(1.23,kg=1,A=-1))

    def test_ge_dimless_and_int_false(self):
        self.assertFalse(CustomValue(1) >= 2)

    def test_ge_dimless_and_int_true(self):
        self.assertTrue(CustomValue(2) >= 1)

    def test_ge_dimless_and_int_eq_true(self):
        self.assertTrue(CustomValue(2) >= 2)

    def test_ge_dimless_and_float_false(self):
        self.assertFalse(CustomValue(1.234) >= 4.321)

    def test_ge_dimless_and_float_true(self):
        self.assertTrue(CustomValue(4.321) >= 1.234)

    def test_ge_dimless_and_float_eq_true(self):
        self.assertTrue(CustomValue(4.321) >= 4.321)

    def test_ge_invalid(self):
        with self.assertRaises(TypeError):
            CustomValue(4.321) >= "invalid"


class CustomValueGreaterThan(unittest.TestCase):
    def test_gt_same_units_false(self):
        self.assertFalse(CustomValue(1.23,kg=1,A=-1) > CustomValue(4.56,kg=1,A=-1))

    def test_gt_same_units_true(self):
        self.assertTrue(CustomValue(4.56,kg=1,A=-1) > CustomValue(1.23,kg=1,A=-1))

    def test_gt_same_units_eq_false(self):
        self.assertFalse(CustomValue(1.23,kg=1,A=-1) > CustomValue(1.23,kg=1,A=-1))

    def test_gt_dimless_and_int_false(self):
        self.assertFalse(CustomValue(1) > 2)

    def test_gt_dimless_and_int_true(self):
        self.assertTrue(CustomValue(2) >= 1)

    def test_gt_dimless_and_int_eq_false(self):
        self.assertFalse(CustomValue(2) > 2)

    def test_gt_dimless_and_float_false(self):
        self.assertFalse(CustomValue(1.234) > 4.321)

    def test_gt_dimless_and_float_true(self):
        self.assertTrue(CustomValue(4.321) > 1.234)

    def test_gt_dimless_and_float_eq_false(self):
        self.assertFalse(CustomValue(1.234) > 1.234)

    def test_gt_invalid(self):
        with self.assertRaises(TypeError):
            CustomValue(4.321) > "invalid"


