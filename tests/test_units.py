import unittest

from unitcalc import Units


class UnitInit(unittest.TestCase):
    def test_init_unit_positive_units(self):
        units = Units(kg=1,A=1,m=1,sec=1,cd=1,K=1,mol=1)
        self.assertIsInstance(units,Units)


    def test_init_unit_negative_units(self):
        units = Units(kg=-1,A=-1,m=-1,sec=-1,cd=-1,K=-1,mol=-1)
        self.assertIsInstance(units,Units)

    def test_init_unit_no_units(self):
        units = Units()
        self.assertIsInstance(units,Units)



class UnitClassMethod(unittest.TestCase):
    def test_empty_units(self):
        self.assertEqual(Units(),Units.empty_units())



class UnitAsDict(unittest.TestCase):
    def test_as_dict_method_positive_units(self):
        units = Units(kg=1,A=1,m=1,sec=1,cd=1,K=1,mol=1)
        units_dict ={"sec":1,"m":1,"kg":1,
                     "K":1,"A":1,"mol":1,
                     "cd":1}
        self.assertEqual(units.as_dict(),units_dict)

    def test_as_dict_method_negative_units(self):
        units = Units(kg=-1,A=-1,m=-1,sec=-1,cd=-1,K=-1,mol=-1)
        units_dict ={"sec":-1,"m":-1,"kg":-1,
                     "K":-1,"A":-1,"mol":-1,
                     "cd":-1}
        self.assertEqual(units.as_dict(),units_dict)

    def test_as_dict_method_no_units(self):
        units = Units()
        units_dict ={"sec":0,"m":0,"kg":0,
                     "K":0,"A":0,"mol":0,
                     "cd":0}
        self.assertEqual(units.as_dict(),units_dict)


class UnitBoolMethods(unittest.TestCase):
    def test_eq(self):
        unit_1 = Units(kg=1,A=1,m=1,sec=1,cd=1,K=1,mol=1)
        unit_2 = Units(kg=1,A=1,m=1,sec=1,cd=1,K=1,mol=1)
        self.assertEqual(unit_1,unit_2)

    def test_ne(self):
        unit_1 = Units(kg=1,A=1,m=1,sec=1,cd=1,K=1,mol=1)
        unit_2 = Units(kg=1,A=1,m=1,sec=0,cd=1,K=1,mol=1)
        self.assertNotEqual(unit_1,unit_2)


class UnitMathMethods(unittest.TestCase):
    units_1 = Units(kg=1,A=1,m=1,sec=1,cd=1,K=1,mol=1)
    units_2 = Units(kg=2,A=-3,m=0,sec=5,cd=2,K=-1,mol=4)

    def test_mult(self):
        units_3 = UnitMathMethods.units_1 * UnitMathMethods.units_2
        mult_result = Units(kg=3,A=-2,m=1,sec=6,cd=3,K=0,mol=5)
        self.assertEqual(mult_result,units_3)

    def test_truediv(self):
        units_3 = UnitMathMethods.units_1 / UnitMathMethods.units_2
        div_result = Units(kg=-1,A=4,m=1,sec=-4,cd=-1,K=2,mol=-3)
        self.assertEqual(div_result,units_3)

    def test_pow(self):
        units_3 = UnitMathMethods.units_2**2
        pow_result = Units(kg=4,A=-6,m=0,sec=10,cd=4,K=-2,mol=8)
        self.assertEqual(pow_result,units_3)


class UnitStrReprMethods(unittest.TestCase):
    
    def test_0_to_6_str(self):
        self.assertEqual(str(Units(kg=0,A=1,m=2,sec=3,cd=4,K=5,mol=6)),
                         "A m² sec³ cd⁴ K⁵ mol⁶")

    def test_7_to_9_str(self):
        self.assertEqual(str(Units(kg=7,A=8,m=9)),
                         "kg⁷ A⁸ m⁹")

    def test_neg_1_to_neg_8_str(self):
        self.assertEqual(str(Units(kg=-1,A=-2,m=-3,sec=-4,cd=-5,K=-6,mol=-7)),
                         "/ kg A² m³ sec⁴ cd⁵ K⁶ mol⁷")

    def test_neg_9_str(self):
        self.assertEqual(str(Units(kg=-8,A=-9)),
                         "/ kg⁸ A⁹")

    def test_decimal_str(self):
        self.assertEqual(str(Units(kg=1.23,A=-4.56)),
                         "kg¹·²³ / A⁴·⁵⁶")

    
    
    def test_0_to_6_repr(self):
        self.assertEqual(Units(kg=0,A=1,m=2,sec=3,cd=4,K=5,mol=6).__repr__(),
                         "A m² sec³ cd⁴ K⁵ mol⁶")

    def test_7_to_9_repr(self):
        self.assertEqual(Units(kg=7,A=8,m=9).__repr__(),
                         "kg⁷ A⁸ m⁹")

    def test_neg_1_to_neg_8_repr(self):
        self.assertEqual(Units(kg=-1,A=-2,m=-3,sec=-4,cd=-5,K=-6,mol=-7).__repr__(),
                         "/ kg A² m³ sec⁴ cd⁵ K⁶ mol⁷")

    def test_neg_9_repr(self):
        self.assertEqual(Units(kg=-8,A=-9).__repr__(),
                         "/ kg⁸ A⁹")

    def test_decimal_repr(self):
        self.assertEqual(Units(kg=1.23,A=-4.56).__repr__(),
                         "kg¹·²³ / A⁴·⁵⁶")


if __name__ == '__main__':
    unittest.main()