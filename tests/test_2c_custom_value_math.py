import unittest
from unitcalc.value_types.value import CustomValue

class CustomValueAdd(unittest.TestCase):
    cv_1 = CustomValue(1,kg=1,m=2)
    cv_2 = CustomValue(2,kg=1,m=2)
    cv_dimless = CustomValue(3.14)
    const_int = 5
    const_float = 5.

    def test_add_same_units(self):
        ans = CustomValue(3,kg=1,m=2)
        test_sum = CustomValueAdd.cv_1 + CustomValueAdd.cv_2
        self.assertEqual(ans,test_sum)


    def test_add_dimensionless_and_const_int(self):
        ans = CustomValue(8.14)
        test_sum = CustomValueAdd.cv_dimless + CustomValueAdd.const_int
        self.assertEqual(ans,test_sum)

    def test_add_dimensionless_and_const_float(self):
        ans = CustomValue(8.14)
        test_sum = CustomValueAdd.cv_dimless + CustomValueAdd.const_float
        self.assertEqual(ans,test_sum)


    def test_add_diff_units_dimless(self):
        with self.assertRaises(ValueError):
            CustomValueAdd.cv_1 + CustomValueAdd.cv_dimless

    def test_add_diff_units_int(self):
        with self.assertRaises(ValueError):
            CustomValueAdd.cv_1 + CustomValueAdd.const_int

    def test_add_diff_units_float(self):
        with self.assertRaises(ValueError):
            CustomValueAdd.cv_1 + CustomValueAdd.const_float


    def test_add_invalid(self):
        with self.assertRaises(AttributeError):
            CustomValueAdd.cv_1 + "invalid"


    def test_radd_dimensionless_and_const_int(self):
        ans = CustomValue(8.14)
        test_sum = CustomValueAdd.const_int + CustomValueAdd.cv_dimless
        self.assertEqual(ans,test_sum)

    def test_radd_dimensionless_and_const_float(self):
        ans = CustomValue(8.14)
        test_sum = CustomValueAdd.const_float + CustomValueAdd.cv_dimless
        self.assertEqual(ans,test_sum)


    def test_radd_diff_units_int(self):
        with self.assertRaises(ValueError):
            CustomValueAdd.const_int + CustomValueAdd.cv_1

    def test_add_diff_units_float(self):
        with self.assertRaises(ValueError):
            CustomValueAdd.const_float + CustomValueAdd.cv_1

    def test_radd_invalid(self):
        with self.assertRaises(AttributeError):
            "invalid" + CustomValueAdd.cv_1


class CustomValueSub(unittest.TestCase):
    cv_1 = CustomValue(1,kg=1,m=2)
    cv_2 = CustomValue(2,kg=1,m=2)
    cv_dimless = CustomValue(3.1)
    const_int = 5
    const_float = 5.

    def test_sub_same_units(self):
        ans = CustomValue(-1,kg=1,m=2)
        test_sum = CustomValueSub.cv_1 - CustomValueSub.cv_2
        self.assertEqual(ans,test_sum)


    def test_sub_dimensionless_and_const_int(self):
        ans = CustomValue(-1.9)
        test_sum = CustomValueSub.cv_dimless - CustomValueSub.const_int
        self.assertEqual(ans,test_sum)

    def test_sub_dimensionless_and_const_float(self):
        ans = CustomValue(-1.9)
        test_sum = CustomValueSub.cv_dimless - CustomValueSub.const_float
        self.assertEqual(ans,test_sum)


    def test_sub_diff_units_dimless(self):
        with self.assertRaises(ValueError):
            CustomValueSub.cv_1 - CustomValueSub.cv_dimless

    def test_sub_diff_units_int(self):
        with self.assertRaises(ValueError):
            CustomValueSub.cv_1 - CustomValueSub.const_int

    def test_sub_diff_units_float(self):
        with self.assertRaises(ValueError):
            CustomValueSub.cv_1 - CustomValueSub.const_float


    def test_sub_invalid(self):
        with self.assertRaises(AttributeError):
            CustomValueSub.cv_1 - "invalid"


    def test_rsub_dimensionless_and_const_int(self):
        ans = CustomValue(1.9)
        test_sum = CustomValueSub.const_int - CustomValueSub.cv_dimless
        self.assertEqual(ans,test_sum)

    def test_rsub_dimensionless_and_const_float(self):
        ans = CustomValue(1.9)
        test_sum = CustomValueSub.const_float - CustomValueSub.cv_dimless
        self.assertEqual(ans,test_sum)


    def test_rsub_diff_units_int(self):
        with self.assertRaises(ValueError):
            CustomValueSub.const_int - CustomValueSub.cv_1

    def test_sub_diff_units_float(self):
        with self.assertRaises(ValueError):
            CustomValueSub.const_float - CustomValueSub.cv_1

    def test_rsub_invalid(self):
        with self.assertRaises(AttributeError):
            "invalid" - CustomValueSub.cv_1



class CustomValueMult(unittest.TestCase):
    cv_1 = CustomValue(2,kg=1,m=2)
    cv_2 = CustomValue(2,kg=-1,A=1,m=2)
    const_int = 5
    const_float = 5.

    def test_mult_with_custom_value(self):
        ans = CustomValueMult.cv_1 * CustomValueMult.cv_2
        self.assertEqual(ans,CustomValue(4,A=1,m=4))

    def test_mult_with_int(self):
        ans = CustomValueMult.cv_1 * CustomValueMult.const_int
        self.assertEqual(ans,CustomValue(10.,kg=1,m=2))

    def test_mult_with_float(self):
        ans = CustomValueMult.cv_1 * CustomValueMult.const_float
        self.assertEqual(ans,CustomValue(10.,kg=1,m=2))

    def test_mult_invalid(self):
        with self.assertRaises(AttributeError):
            CustomValueMult.cv_1 * "invalid"

    def test_rmult_with_int(self):
        ans = CustomValueMult.const_int * CustomValueMult.cv_1
        self.assertEqual(ans,CustomValue(10.,kg=1,m=2))

    def test_rmult_with_float(self):
        ans = CustomValueMult.const_float * CustomValueMult.cv_1
        self.assertEqual(ans,CustomValue(10.,kg=1,m=2))

    def test_rmult_invalid(self):
        with self.assertRaises(AttributeError):
            "invalid" * CustomValueMult.cv_1
