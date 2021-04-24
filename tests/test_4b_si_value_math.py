import unittest
from unitcalc.value_types.value import SIValue, CustomValue

## Test Classes ##
class SIValueAllPositive(SIValue):
    _re_pattern = "^[Aa]ll[Pp]os(itive)?$"
    def __init__(self,value,prefix:str=""):
        super().__init__(value,prefix=prefix,
                               kg=1,A=1,m=1,sec=1,cd=1,K=1,mol=1)

    def _base_symbol(self):
        return "AllPos"

class SIValueAllNegative(SIValue):
    _re_pattern = "^[Aa]ll[Nn]eg(ative)?$"
    def __init__(self,value,prefix:str=""):
        super().__init__(value,prefix=prefix,
                               kg=-1,A=-1,m=-1,sec=-1,cd=-1,K=-1,mol=-1)

    def _base_symbol(self):
        return "AllNeg"
## Test Classes ##

## Tests ##
class SIValueAdd(unittest.TestCase):
    def test_add_same_units(self):
        ans = SIValueAllPositive(2.46)
        self.assertEqual(ans,SIValueAllPositive(1.23) + SIValueAllPositive(1.23))

    def test_add_diff_units(self):
        with self.assertRaises(ValueError):
            SIValueAllPositive(1.23) + SIValueAllNegative(1.23)

    def test_add_invalid(self):
        with self.assertRaises(AttributeError):
            SIValueAllPositive(1.23) + "invalid"

class SIValueRAdd(unittest.TestCase):
    def test_radd_invalid(self):
        with self.assertRaises(AttributeError):
            "invalid" + SIValueAllPositive(1.23)


class SIValueSub(unittest.TestCase):
    def test_sub_same_units(self):
        ans = SIValueAllPositive(0)
        self.assertEqual(ans,SIValueAllPositive(1.23) - SIValueAllPositive(1.23))

    def test_sub_diff_units(self):
        with self.assertRaises(ValueError):
            SIValueAllPositive(1.23) - SIValueAllNegative(1.23)

    def test_sub_invalid(self):
        with self.assertRaises(AttributeError):
            SIValueAllPositive(1.23) - "invalid"

class SIValueRSub(unittest.TestCase):
    def test_rsub_invalid(self):
        with self.assertRaises(AttributeError):
            "invalid" - SIValueAllPositive(1.23)


class SIValueMult(unittest.TestCase):
    def test_mult_with_int(self):
        ans = SIValueAllPositive(2.46)
        self.assertEqual(ans,SIValueAllPositive(1.23) * 2)

    def test_mult_with_float(self):
        ans = SIValueAllPositive(2.46)
        self.assertEqual(ans,SIValueAllPositive(1.23) * 2.)

    def test_mult_same_units(self):
        ans = CustomValue(2.46,kg=2,A=2,m=2,sec=2,cd=2,K=2,mol=2)
        self.assertEqual(ans,SIValueAllPositive(2) * SIValueAllPositive(1.23))

    def test_mult_diff_units(self):
        ans = CustomValue(2.46)
        self.assertEqual(ans,SIValueAllPositive(2) * SIValueAllNegative(1.23))

    def test_mult_invalid(self):
        with self.assertRaises(AttributeError):
            SIValueAllPositive(1.23) * "invalid"

class SIValueRMult(unittest.TestCase):
    def test_rmult_with_int(self):
        ans = SIValueAllPositive(2.46)
        self.assertEqual(ans,2 * SIValueAllPositive(1.23))

    def test_rmult_with_float(self):
        ans = SIValueAllPositive(2.46)
        self.assertEqual(ans,2. * SIValueAllPositive(1.23))

    def test_rmult_invalid(self):
        with self.assertRaises(AttributeError):
            "invalid" * SIValueAllPositive(1.23)


class SIValueTrueDiv(unittest.TestCase):
    def test_div_with_int(self):
        ans = SIValueAllPositive(1.23)
        self.assertEqual(ans,SIValueAllPositive(2.46) / 2)

    def test_div_with_float(self):
        ans = SIValueAllPositive(1.23)
        self.assertEqual(ans,SIValueAllPositive(2.46) / 2.)

    def test_div_same_units(self):
        ans = CustomValue(2)
        self.assertEqual(ans,SIValueAllPositive(2.46) / SIValueAllPositive(1.23))

    def test_div_diff_units(self):
        ans = CustomValue(2,kg=2,A=2,m=2,sec=2,cd=2,K=2,mol=2)
        self.assertEqual(ans,SIValueAllPositive(2.46) / SIValueAllNegative(1.23))

    def test_div_invalid(self):
        with self.assertRaises(AttributeError):
            SIValueAllPositive(1.23) / "invalid"

class SIValueRTrueDiv(unittest.TestCase):
    def test_rdiv_with_int(self):
        ans = SIValueAllNegative(2.)
        self.assertEqual(ans,4 / SIValueAllPositive(2.))

    def test_rdiv_with_float(self):
        ans = SIValueAllNegative(2)
        self.assertEqual(ans,4. / SIValueAllPositive(2.))

    def test_rdiv_invalid(self):
        with self.assertRaises(AttributeError):
            "invalid" / SIValueAllPositive(1.23)


class SIValuePow(unittest.TestCase):
    def test_pow_int(self):
        ans = CustomValue(4,kg=2,A=2,m=2,sec=2,cd=2,K=2,mol=2)
        self.assertEqual(ans,SIValueAllPositive(2)**2)

    def test_pow_float(self):
        ans = CustomValue(4.,kg=2,A=2,m=2,sec=2,cd=2,K=2,mol=2)
        self.assertEqual(ans,SIValueAllPositive(2)**2.)

    def test_pow_invalid(self):
        with self.assertRaises(AttributeError):
            SIValueAllPositive(2.)**"invalid"

