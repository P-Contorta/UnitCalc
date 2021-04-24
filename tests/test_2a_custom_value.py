import unittest

from unitcalc import Units
from unitcalc.value_types.value import CustomValue

class CustomValueIsValueMethod(unittest.TestCase):
    def test_is_value(self):
        test_names = ("kg, Kilogram, meter, Celcius, Pound, cd, mol, Amps")
        for name in test_names:
            self.assertFalse(CustomValue.is_value(name))


class CustomValueInit(unittest.TestCase):
    def test_init_invalid_value(self):
        with self.assertRaises(AttributeError):
            CustomValue('invalid')

    def test_init_dimensionless(self):
        value_types = (1,1.0)
        for value_type in value_types:
            self.assertIsInstance(CustomValue(value_type),
                                  CustomValue)

    def test_init_all_positive(self):
        value_types = (1,1.0)
        for value_type in value_types:
            self.assertIsInstance(CustomValue(value_type,
                                              kg=1,A=1,m=1,sec=1,cd=1,K=1,mol=1),
                                  CustomValue)

    def test_init_all_negative(self):
        value_types = (1,1.0)
        for value_type in value_types:
            self.assertIsInstance(CustomValue(value_type,
                                              kg=-1,A=-1,m=-1,sec=-1,cd=-1,K=-1,mol=-1),
                                  CustomValue)


class CustomValueValueMethods(unittest.TestCase):
    cv = CustomValue(1.23,kg=1,A=1,m=1,sec=1,cd=1,K=1,mol=1)

    def test_value_method(self):
        self.assertEqual(1.23, 
                         CustomValueValueMethods.cv.value())
        
    def test_si_value_method(self):
        self.assertEqual(1.23,
                         CustomValueValueMethods.cv.si_value())

    def test_central_value_method(self):
        self.assertEqual(1.23,
                         CustomValueValueMethods.cv.central_value())


class CustomValueSIUnitsMethod(unittest.TestCase):
    def test_si_units_method_all_positive(self):
        cv = CustomValue(1.23,kg=1,A=1,m=1,sec=1,cd=1,K=1,mol=1)
        units = Units(kg=1,A=1,m=1,sec=1,cd=1,K=1,mol=1)
        self.assertEqual(cv.si_units(),units)

    def test_si_units_method_all_negative(self):
        cv = CustomValue(1.23,kg=-1,A=-1,m=-1,sec=-1,cd=-1,K=-1,mol=-1)
        units = Units(kg=-1,A=-1,m=-1,sec=-1,cd=-1,K=-1,mol=-1)
        self.assertEqual(cv.si_units(),units)


    def test_si_units_method_no_units(self):
        cv = CustomValue(1.23)
        units = Units()
        self.assertEqual(cv.si_units(),units)


class CustomValueSymbols(unittest.TestCase):
    cv = CustomValue(1.23,A=1,m=3,sec=-2,K=-1)
    units_test = Units(A=1,m=3,sec=-2,K=-1)
    def test_symbol_method(self):
        self.assertEqual(CustomValueSymbols.cv.symbol(),
                         str(CustomValueSymbols.units_test))

    def test_si_symbol_method(self):
        self.assertEqual(CustomValueSymbols.cv.si_symbol(),
                         str(CustomValueSymbols.units_test))


class CustomValueStrReprMethods(unittest.TestCase):
    def test_str_with_units(self):
        self.assertEqual(str(CustomValue(1.23,A=1,m=3,sec=-2,K=-1)),
                         "{} {}".format(1.23,Units(A=1,m=3,sec=-2,K=-1)))

    def test_str_without_units(self):
        self.assertEqual(str(CustomValue(1.23)),str(1.23))

    def test_repr_with_units(self):
        self.assertEqual(CustomValue(1.23,A=1,m=3,sec=-2,K=-1).__repr__(),
                         "{} {}".format(1.23,Units(A=1,m=3,sec=-2,K=-1)))

    def test_repr_without_units(self):
        self.assertEqual(CustomValue(1.23).__repr__(),str(1.23))
