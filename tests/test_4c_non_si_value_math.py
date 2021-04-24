import unittest
from unitcalc.value_types.value import NonSIValue, SIValue, CustomValue

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
class NonSIValueAdd(unittest.TestCase):
    def test_add_same_units(self):
        ans = NonSIValueAllPositive(2.46)
        self.assertEqual(ans,NonSIValueAllPositive(1.23) + NonSIValueAllPositive(1.23))

    def test_add_diff_units(self):
        with self.assertRaises(ValueError):
            NonSIValueAllPositive(1.23) + NonSIValueAllNegative(1.23)

    def test_add_invalid(self):
        with self.assertRaises(AttributeError):
            NonSIValueAllPositive(1.23) + "invalid"

class NonSIValueRAdd(unittest.TestCase):
    def test_radd_invalid(self):
        with self.assertRaises(AttributeError):
            "invalid" + NonSIValueAllPositive(1.23)


class NonSIValueSub(unittest.TestCase):
    def test_sub_same_units(self):
        ans = NonSIValueAllPositive(0)
        self.assertEqual(ans,NonSIValueAllPositive(1.23) - NonSIValueAllPositive(1.23))

    def test_sub_diff_units(self):
        with self.assertRaises(ValueError):
            NonSIValueAllPositive(1.23) - NonSIValueAllNegative(1.23)

    def test_sub_invalid(self):
        with self.assertRaises(AttributeError):
            NonSIValueAllPositive(1.23) - "invalid"

class NonSIValueRSub(unittest.TestCase):
    def test_rsub_invalid(self):
        with self.assertRaises(AttributeError):
            "invalid" - NonSIValueAllPositive(1.23)

#### HERE ####
class NonSIValueMult(unittest.TestCase):
    def test_mult_with_int(self):
        ans = NonSIValueAllPositive(2.46)
        self.assertEqual(ans,NonSIValueAllPositive(1.23) * 2)

    def test_mult_with_float(self):
        ans = NonSIValueAllPositive(2.46)
        self.assertEqual(ans,NonSIValueAllPositive(1.23) * 2.)

    def test_mult_same_units(self):
        ans = CustomValue(246,kg=2,A=2,m=2,sec=2,cd=2,K=2,mol=2)
        self.assertEqual(ans,NonSIValueAllPositive(2) * NonSIValueAllPositive(1.23))

    def test_mult_diff_units(self):
        ans = CustomValue(246)
        self.assertEqual(ans,NonSIValueAllPositive(2) * NonSIValueAllNegative(1.23))

    def test_mult_invalid(self):
        with self.assertRaises(AttributeError):
            NonSIValueAllPositive(1.23) * "invalid"

class NonSIValueRMult(unittest.TestCase):
    def test_rmult_with_int(self):
        ans = NonSIValueAllPositive(2.46)
        self.assertEqual(ans,2 * NonSIValueAllPositive(1.23))

    def test_rmult_with_float(self):
        ans = NonSIValueAllPositive(2.46)
        self.assertEqual(ans,2. * NonSIValueAllPositive(1.23))

    def test_rmult_invalid(self):
        with self.assertRaises(AttributeError):
            "invalid" * NonSIValueAllPositive(1.23)


class NonSIValueTrueDiv(unittest.TestCase):
    def test_div_with_int(self):
        ans = NonSIValueAllPositive(1.23)
        self.assertEqual(ans,NonSIValueAllPositive(2.46) / 2)

    def test_div_with_float(self):
        ans = NonSIValueAllPositive(1.23)
        self.assertEqual(ans,NonSIValueAllPositive(2.46) / 2.)

    def test_div_same_units(self):
        ans = CustomValue(2)
        self.assertEqual(ans,NonSIValueAllPositive(2.46) / NonSIValueAllPositive(1.23))

    def test_div_diff_units(self):
        ans = CustomValue(2,kg=2,A=2,m=2,sec=2,cd=2,K=2,mol=2)
        self.assertEqual(ans,NonSIValueAllPositive(2.46) / NonSIValueAllNegative(1.23))

    def test_div_invalid(self):
        with self.assertRaises(AttributeError):
            NonSIValueAllPositive(1.23) / "invalid"

class NonSIValueRTrueDiv(unittest.TestCase):
    def test_rdiv_with_int(self):
        ans = NonSIValueAllNegative(.02)
        self.assertEqual(ans,4 / NonSIValueAllPositive(2.))

    def test_rdiv_with_float(self):
        ans = NonSIValueAllNegative(.02)
        self.assertEqual(ans,4. / NonSIValueAllPositive(2.))

    def test_rdiv_invalid(self):
        with self.assertRaises(AttributeError):
            "invalid" / NonSIValueAllPositive(1.23)


class NonSIValuePow(unittest.TestCase):
    def test_pow_int(self):
        ans = CustomValue(400,kg=2,A=2,m=2,sec=2,cd=2,K=2,mol=2)
        self.assertEqual(ans,NonSIValueAllPositive(2)**2)

    def test_pow_float(self):
        ans = CustomValue(400.,kg=2,A=2,m=2,sec=2,cd=2,K=2,mol=2)
        self.assertEqual(ans,NonSIValueAllPositive(2)**2.)

    def test_pow_invalid(self):
        with self.assertRaises(AttributeError):
            NonSIValueAllPositive(2.)**"invalid"