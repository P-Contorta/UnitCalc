import unittest
from unitcalc.value_types.value import NonSIValue, SIValue

## Test Classes ##
class SIValueParentPos(SIValue):
    _re_pattern = "^[Ss][Ii]([Pp]arent[Pp]os)?$"

    def __init__(self,value,prefix:str=""):
        super().__init__(value,prefix=prefix,
                               kg=1,A=1,m=1,sec=1,cd=1,K=1,mol=1)

    def _base_symbol(self):
        return "SIValuePos"

    def convert_to_unit(self,unit_name:str):
        if SIValueParentPos.is_value(unit_name):
            return self
        elif NonSIValueAllPositive.is_value(unit_name):
            return NonSIValueAllPositive(self.central_value() /10)
        else:
            raise ValueError("Cannot convert to {}.".format(unit_name))

class NonSIValueAllPositive(NonSIValue):
    _re_pattern = "^[Nn]onSIValuePos$"

    def __init__(self,value):
        super().__init__(value,SIValueParentPos(value * 10),
                               kg=1,A=1,m=1,sec=1,cd=1,K=1,mol=1)

    def _base_symbol(self):
        return "NonSIValuePos"

    
class SIValueParentNeg(SIValue):
    _re_pattern = "^[Ss][Ii]([Pp]arent[Nn]eg)?$"

    def __init__(self,value,prefix:str=""):
        super().__init__(value,prefix=prefix,
                               kg=-1,A=-1,m=-1,sec=-1,cd=-1,K=-1,mol=-1)

    def _base_symbol(self):
        return "SIValueNeg"

    def convert_to_unit(self,unit_name:str):
        if SIValueParentPos.is_value(unit_name):
            return self
        elif NonSIValueAllPositive.is_value(unit_name):
            return NonSIValueAllPositive(self.central_value() /10)
        else:
            raise ValueError("Cannot convert to {}.".format(unit_name))

class NonSIValueAllNegative(NonSIValue):
    _re_pattern = "^[Nn]onSIValueNeg$"

    def __init__(self,value):
        super().__init__(value,SIValueParentNeg(value * 10),
                               kg=-1,A=-1,m=-1,sec=-1,cd=-1,K=-1,mol=-1)

    def _base_symbol(self):
        return "NonSIValueNeg"
## Test Classes ##

## Tests ##
class NonSIValueEquals(unittest.TestCase):
    def test_eq_same_units_same_values(self):
        self.assertTrue(NonSIValueAllPositive(1.23) == NonSIValueAllPositive(1.23))

    def test_eq_same_units_diff_values(self):
        self.assertFalse(NonSIValueAllPositive(1.23) == NonSIValueAllPositive(3.21))

    def test_eq_diff_units_same_values(self):
        self.assertFalse(NonSIValueAllPositive(1.23) == NonSIValueAllNegative(1.23))

    def test_eq_diff_object_invalid(self):
        self.assertFalse(NonSIValueAllPositive(1.23) == "str-type")

class NonSIValueNotEquals(unittest.TestCase):
    def test_ne_same_units_same_values(self):
        self.assertFalse(NonSIValueAllPositive(1.23) != NonSIValueAllPositive(1.23))

    def test_ne_same_units_diff_values(self):
        self.assertTrue(NonSIValueAllPositive(1.23) != NonSIValueAllPositive(3.21))

    def test_ne_diff_units_same_values(self):
        self.assertTrue(NonSIValueAllPositive(1.23) != NonSIValueAllNegative(1.23))

    def test_ne_diff_object_invalid(self):
        self.assertTrue(NonSIValueAllPositive(1.23) != "str-type")

class NonSIValueLessThan(unittest.TestCase):
    def test_lt_same_units_true(self):
        self.assertTrue(NonSIValueAllPositive(1.23) < NonSIValueAllPositive(3.21))

    def test_lt_same_units_false(self):
        self.assertFalse(NonSIValueAllPositive(3.21) < NonSIValueAllPositive(1.23))

    def test_lt_same_units_value_eq(self):
        self.assertFalse(NonSIValueAllPositive(1.23) < NonSIValueAllPositive(1.23))

    def test_lt_diff_units(self):
        with self.assertRaises(ValueError):
            NonSIValueAllPositive(1.23) < NonSIValueAllNegative(3.21)

    def test_lt_diff_object_invalid(self):
        with self.assertRaises(TypeError):
            NonSIValueAllPositive(1.23) < "invalid-type"

class NonSIValueGreaterThan(unittest.TestCase):
    def test_gt_same_units_true(self):
        self.assertTrue(NonSIValueAllPositive(3.21) > NonSIValueAllPositive(1.23))

    def test_gt_same_units_false(self):
        self.assertFalse(NonSIValueAllPositive(1.23) > NonSIValueAllPositive(3.21))

    def test_gt_same_units_value_eq(self):
        self.assertFalse(NonSIValueAllPositive(1.23) > NonSIValueAllPositive(1.23))

    def test_gt_diff_units(self):
        with self.assertRaises(ValueError):
            NonSIValueAllNegative(3.21) > NonSIValueAllPositive(1.23)

    def test_gt_diff_object_invalid(self):
        with self.assertRaises(TypeError):
            NonSIValueAllPositive(1.23) > "invalid-type"

class NonSIValueGreaterThanEqual(unittest.TestCase):
    def test_ge_same_units_true(self):
        self.assertTrue(NonSIValueAllPositive(3.21) >= NonSIValueAllPositive(1.23))

    def test_ge_same_units_false(self):
        self.assertFalse(NonSIValueAllPositive(1.23) >= NonSIValueAllPositive(3.21))

    def test_ge_same_units_value_eq(self):
        self.assertTrue(NonSIValueAllPositive(1.23) >= NonSIValueAllPositive(1.23))

    def test_ge_diff_units(self):
        with self.assertRaises(ValueError):
            NonSIValueAllNegative(3.21) >= NonSIValueAllPositive(1.23)

    def test_ge_diff_object_invalid(self):
        with self.assertRaises(TypeError):
            NonSIValueAllPositive(1.23) >= "invalid-type"

class NonSIValueLessThanEqual(unittest.TestCase):
    def test_le_same_units_true(self):
        self.assertTrue(NonSIValueAllPositive(1.23) <= NonSIValueAllPositive(3.21))

    def test_le_same_units_false(self):
        self.assertFalse(NonSIValueAllPositive(3.21) <= NonSIValueAllPositive(1.23))

    def test_le_same_units_value_eq(self):
        self.assertTrue(NonSIValueAllPositive(1.23) <= NonSIValueAllPositive(1.23))

    def test_le_diff_units(self):
        with self.assertRaises(ValueError):
            NonSIValueAllPositive(1.23) <= NonSIValueAllNegative(3.21)

    def test_le_diff_object_invalid(self):
        with self.assertRaises(TypeError):
            NonSIValueAllPositive(1.23) <= "invalid-type"