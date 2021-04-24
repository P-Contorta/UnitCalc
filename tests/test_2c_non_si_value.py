import unittest

from unitcalc import Units
from unitcalc.value_types.value import NonSIValue, SIValue
## Test classes ##
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

class SIValueParentPosPrefixKilo(SIValue):
    _re_pattern = "^[Ss][Ii]([Pp]arent)?Prefix$"

    def __init__(self,value,prefix:str="kilo"):
        super().__init__(value,prefix=prefix,
                               kg=1,A=1,m=1,sec=1,cd=1,K=1,mol=1)

    def _base_symbol(self):
        return "SIValuePosPrefixKilo"

    def convert_to_unit(self,unit_name:str):
        if SIValueParentPos.is_value(unit_name):
            return self
        elif NonSIValueAllPositive.is_value(unit_name):
            return NonSIValueAllPositive(self.central_value() /10)
        else:
            raise ValueError("Cannot convert to {}.".format(unit_name))


class NonSIValueAllPositivePrefixKilo(NonSIValue):
    _re_pattern = "^[Nn]onSIValuePosPrefixKilo$"

    def __init__(self,value):
        super().__init__(value,SIValueParentPosPrefixKilo(value * 10),
                               kg=1,A=1,m=1,sec=1,cd=1,K=1,mol=1)

    def _base_symbol(self):
        return "NonSIValuePosPrefixKilo"


class SIValueParentPosCenterKilo(SIValue):
    _re_pattern = "^[Ss][Ii]([Pp]arent)?Center$"

    def __init__(self,value,prefix:str=""):
        super().__init__(value,prefix=prefix,center_prefix="kilo",
                               kg=1,A=1,m=1,sec=1,cd=1,K=1,mol=1)

    def _base_symbol(self):
        return "SIValuePosKiloCenter"

    def convert_to_unit(self,unit_name:str):
        if SIValueParentPos.is_value(unit_name):
            return self
        elif NonSIValueAllPositive.is_value(unit_name):
            return NonSIValueAllPositive(self.central_value() /10)
        else:
            raise ValueError("Cannot convert to {}.".format(unit_name))


class NonSIValueAllPositiveCenterKilo(NonSIValue):
    _re_pattern = "^[Nn]onSIValuePosCenterKilo$"

    def __init__(self,value):
        super().__init__(value,SIValueParentPosCenterKilo(value * 10),
                               kg=1,A=1,m=1,sec=1,cd=1,K=1,mol=1)

    def _base_symbol(self):
        return "NonSIValuePosCenterKilo"
## Test classes ##



## Begin tests ##
class NonSIValueIsValuePreInit(unittest.TestCase):
    def test_is_value_no_overload(self):
        with self.assertRaises(NotImplementedError):
            NonSIValue.is_value("not-implemented")


    def test_is_value_overload_true(self):
        self.assertTrue(NonSIValueAllPositive.is_value("nonSIValuePos"))

    def test_is_value_overload_false(self):
        self.assertFalse(NonSIValueAllPositive.is_value("<false>"))


class NonSIValueInit(unittest.TestCase):
    def test_init_invalid_value(self):
        with self.assertRaisesRegex(AttributeError,
                                    "NonSIValue only takes int or float as input for value\."):
            NonSIValue('invalid_value',"invalid_si_parent")


    def test_init_invalid_si_parent(self):
        for value_type in (1,1.0):
            with self.assertRaisesRegex(AttributeError,
                                        "NonSIValue only takes SIValue as input for si_parent\."):
                NonSIValue(value_type,"invalid_si_parent")


    def test_base_symbol_not_implemented(self):
        with self.assertRaises(NotImplementedError):
            NonSIValue(1,SIValueParentPos(10))


    def test_init_dimensionless(self):
        for value_type in (1,1.0):
            self.assertIsInstance(NonSIValueAllPositive(value_type),
                                  NonSIValue)

    def test_init_all_positive(self):
        for value_type in (1,1.0):
            self.assertIsInstance(NonSIValueAllPositive(value_type),
                                  NonSIValue)

    def test_init_all_negative(self):
        for value_type in (1,1.0):
            self.assertIsInstance(NonSIValueAllPositive(value_type),
                                  NonSIValue)


class NonSIValueValueMethods(unittest.TestCase):
    def test_value_method(self):
        self.assertEqual(1.23, NonSIValueAllPositive(1.23).value())
        
    def test_si_value_method(self):
        self.assertEqual(12.3, NonSIValueAllPositive(1.23).si_value())

    def test_central_value_method(self):
        self.assertEqual(12.3, NonSIValueAllPositive(1.23).central_value())


    def test_value_method_si_parent_kilo_center(self):
        self.assertEqual(1.23, NonSIValueAllPositiveCenterKilo(1.23).value())

    def test_si_value_method_si_parent_kilo_center(self):
        self.assertEqual(12.3,
                         NonSIValueAllPositiveCenterKilo(1.23).si_value())

    def test_central_value_method_si_parent_kilo_center(self):
        self.assertEqual(12.3*10**-3,
                         NonSIValueAllPositiveCenterKilo(1.23).central_value())


class NonSIValueSIUnitsMethod(unittest.TestCase):
    def test_si_units_method(self):
        self.assertEqual(NonSIValueAllPositive(1.23).si_units(),
                         Units(kg=1,A=1,m=1,sec=1,cd=1,K=1,mol=1))


class NonSIValueSymbols(unittest.TestCase):
    def test_symbol_method(self):
        self.assertEqual(NonSIValueAllPositive(1.23).symbol(),
                         "NonSIValuePos")

    def test_si_symbol_method(self):
        self.assertEqual(NonSIValueAllPositive(1.23).si_symbol(),
                         "SIValuePos")

    def test_symbol_method_kilo_prefix(self):
        self.assertEqual(NonSIValueAllPositivePrefixKilo(1.23).symbol(),
                         "NonSIValuePosPrefixKilo")

    def test_si_symbol_method_kilo_prefix(self):
        self.assertEqual(NonSIValueAllPositivePrefixKilo(1.23).si_symbol(),
                         "kSIValuePosPrefixKilo")


    def test_symbol_method_kilo_center_prefix(self):
        self.assertEqual(NonSIValueAllPositiveCenterKilo(1.23).symbol(),
                         "NonSIValuePosCenterKilo")

    def test_si_symbol_method_kilo_center_prefix(self):
        self.assertEqual(NonSIValueAllPositiveCenterKilo(1.23).si_symbol(),
                         "SIValuePosKiloCenter")


class NonSIValueConvertToUnit(unittest.TestCase):
    # Can assertEqual the two objects because the __eq__ meth hasn't been tested yet
    def test_convert_to_self(self):
        si_v_parent = SIValueParentPos(12.3)
        non_si_v = NonSIValueAllPositive(1.23)
        si_v_parent2 = non_si_v.convert_to_unit('SIParentPos')
        self.assertEqual(si_v_parent.value(),si_v_parent2.value())
        self.assertEqual(si_v_parent.symbol(),si_v_parent2.symbol())
        self.assertEqual(si_v_parent.si_units(),si_v_parent2.si_units())

    def test_convert_to_invalid(self):
        with self.assertRaises(ValueError):
            NonSIValueAllPositive(1.23).convert_to_unit("<invalid>")


class SIValueStrReprMethods(unittest.TestCase):
    def test_str(self):
        self.assertEqual(str(NonSIValueAllPositive(1.23)),
                         "{} {}".format(1.23,"NonSIValuePos"))

    def test_repr(self):
        self.assertEqual(NonSIValueAllPositive(1.23).__repr__(),
                         "{} {}".format(1.23,"NonSIValuePos"))