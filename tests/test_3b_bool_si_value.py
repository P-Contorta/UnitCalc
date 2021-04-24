import unittest
from unitcalc.value_types.value import SIValue

## Test Classes ##
class SIValueAllPositive(SIValue):
    _re_pattern = "^[Aa]ll[Pp]os(itive)?$"
    def __init__(self,value,prefix:str="",parser=None):
        super().__init__(value,prefix=prefix,
                               kg=1,A=1,m=1,sec=1,cd=1,K=1,mol=1,
                               parser=parser)

    def _base_symbol(self):
        return "AllPos"



class SIValueAllNegative(SIValue):
    _re_pattern = "^[Aa]ll[Nn]eg(ative)?$"
    def __init__(self,value,prefix:str="",parser=None):
        super().__init__(value,prefix=prefix,
                               kg=-1,A=-1,m=-1,sec=-1,cd=-1,K=-1,mol=-1,
                               parser=parser)

    def _base_symbol(self):
        return "AllNeg"
## Test Classes ##

## Tests ##
class SIValueEquals(unittest.TestCase):
    def test_eq_same_units_same_values(self):
        self.assertTrue(SIValueAllPositive(1.23) == SIValueAllPositive(1.23))

    def test_eq_same_units_diff_values(self):
        self.assertFalse(SIValueAllPositive(1.23) == SIValueAllPositive(3.21))

    def test_eq_diff_units_same_values(self):
        self.assertFalse(SIValueAllPositive(1.23) == SIValueAllNegative(1.23))

    def test_eq_diff_object_invalid(self):
        self.assertFalse(SIValueAllPositive(1.23) == "str-type")

class SIValueNotEquals(unittest.TestCase):
    def test_ne_same_units_same_values(self):
        self.assertFalse(SIValueAllPositive(1.23) != SIValueAllPositive(1.23))

    def test_ne_same_units_diff_values(self):
        self.assertTrue(SIValueAllPositive(1.23) != SIValueAllPositive(3.21))

    def test_ne_diff_units_same_values(self):
        self.assertTrue(SIValueAllPositive(1.23) != SIValueAllNegative(1.23))

    def test_ne_diff_object_invalid(self):
        self.assertTrue(SIValueAllPositive(1.23) != "str-type")

class SIValueLessThan(unittest.TestCase):
    def test_lt_same_units_true(self):
        self.assertTrue(SIValueAllPositive(1.23) < SIValueAllPositive(3.21))

    def test_lt_same_units_false(self):
        self.assertFalse(SIValueAllPositive(3.21) < SIValueAllPositive(1.23))

    def test_lt_same_units_value_eq(self):
        self.assertFalse(SIValueAllPositive(1.23) < SIValueAllPositive(1.23))

    def test_lt_diff_units(self):
        with self.assertRaises(ValueError):
            SIValueAllPositive(1.23) < SIValueAllNegative(3.21)

    def test_lt_diff_object_invalid(self):
        with self.assertRaises(TypeError):
            SIValueAllPositive(1.23) < "invalid-type"

class SIValueGreaterThan(unittest.TestCase):
    def test_gt_same_units_true(self):
        self.assertTrue(SIValueAllPositive(3.21) > SIValueAllPositive(1.23))

    def test_gt_same_units_false(self):
        self.assertFalse(SIValueAllPositive(1.23) > SIValueAllPositive(3.21))

    def test_gt_same_units_value_eq(self):
        self.assertFalse(SIValueAllPositive(1.23) > SIValueAllPositive(1.23))

    def test_gt_diff_units(self):
        with self.assertRaises(ValueError):
            SIValueAllNegative(3.21) > SIValueAllPositive(1.23)

    def test_gt_diff_object_invalid(self):
        with self.assertRaises(TypeError):
            SIValueAllPositive(1.23) > "invalid-type"

class SIValueGreaterThanEqual(unittest.TestCase):
    def test_ge_same_units_true(self):
        self.assertTrue(SIValueAllPositive(3.21) >= SIValueAllPositive(1.23))

    def test_ge_same_units_false(self):
        self.assertFalse(SIValueAllPositive(1.23) >= SIValueAllPositive(3.21))

    def test_ge_same_units_value_eq(self):
        self.assertTrue(SIValueAllPositive(1.23) >= SIValueAllPositive(1.23))

    def test_ge_diff_units(self):
        with self.assertRaises(ValueError):
            SIValueAllNegative(3.21) >= SIValueAllPositive(1.23)

    def test_ge_diff_object_invalid(self):
        with self.assertRaises(TypeError):
            SIValueAllPositive(1.23) >= "invalid-type"

class SIValueLessThanEqual(unittest.TestCase):
    def test_le_same_units_true(self):
        self.assertTrue(SIValueAllPositive(1.23) <= SIValueAllPositive(3.21))

    def test_le_same_units_false(self):
        self.assertFalse(SIValueAllPositive(3.21) <= SIValueAllPositive(1.23))

    def test_le_same_units_value_eq(self):
        self.assertTrue(SIValueAllPositive(1.23) <= SIValueAllPositive(1.23))

    def test_le_diff_units(self):
        with self.assertRaises(ValueError):
            SIValueAllPositive(1.23) <= SIValueAllNegative(3.21)

    def test_le_diff_object_invalid(self):
        with self.assertRaises(TypeError):
            SIValueAllPositive(1.23) <= "invalid-type"