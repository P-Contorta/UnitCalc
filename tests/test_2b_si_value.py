import unittest

from unitcalc import Units
from unitcalc.value_types.value import SIValue


## Test classes ##
class SIValueAllPositive(SIValue):
    _re_pattern = "^[Aa]ll[Pp]os(itive)?$"
    def __init__(self,value,prefix:str=""):
        super().__init__(value,prefix=prefix,
                               kg=1,A=1,m=1,sec=1,cd=1,K=1,mol=1)

    def _base_symbol(self):
        return "AllPos"

class SIValueAllPositiveKilo(SIValue):
    _re_pattern = "^[Aa]ll$|^[Aa]ll[Pp]os(itive)?[Kk]ilo$"
    def __init__(self,value,prefix:str=""):
        super().__init__(value,prefix=prefix,center_prefix="kilo",
                               kg=1,A=1,m=1,sec=1,cd=1,K=1,mol=1)

    def _base_symbol(self):
        return "AllPosKilo"        

class SIValueAllNegative(SIValue):
    _re_pattern = "^[Aa]ll[Nn]eg(ative)?$"
    def __init__(self,value,prefix:str=""):
        super().__init__(value,prefix=prefix,
                               kg=-1,A=-1,m=-1,sec=-1,cd=-1,K=-1,mol=-1)

    def _base_symbol(self):
        return "AllNeg"

class SIValueDimless(SIValue):
    _re_pattern = "^[Dd]im(less)?$"
    def __init__(self,value,prefix:str=""):
        super().__init__(value,prefix=prefix)

    def _base_symbol(self):
        return "Dimless"
## Test classes ##


## Begin tests ##
class SIValueIsValuePreInit(unittest.TestCase):
    def test_is_value_no_overload(self):
        with self.assertRaises(NotImplementedError):
            SIValue.is_value("not-implemented")

    def test_is_value_overload_true(self):
        self.assertTrue(SIValueAllPositive.is_value("AllPos"))

    def test_is_value_overload_false(self):
        self.assertFalse(SIValueAllPositive.is_value("AllNeg"))


class SIValueInit(unittest.TestCase):
    def test_init_invalid_value(self):
        with self.assertRaises(AttributeError):
            SIValue('invalid')

    def test_base_symbol_not_implemented(self):
        with self.assertRaises(NotImplementedError):
            SIValue(1)

    def test_init_dimensionless(self):
        for value_type in (1,1.0):
            self.assertIsInstance(SIValueDimless(value_type),SIValue)

    def test_init_all_positive(self):
        for value_type in (1,1.0):
            self.assertIsInstance(SIValueAllPositive(value_type),SIValue)

    def test_init_all_negative(self):
        for value_type in (1,1.0):
            self.assertIsInstance(SIValueAllNegative(value_type), SIValue)


class SIValuePrefixParsing(unittest.TestCase):
    def test_prefix_yocto(self):
        prefix_tester = SIValueDimless(0)
        for prefix in ("y","yocto","Yocto"):
            self.assertEqual(prefix_tester._parse_prefix(prefix),
                             ("y",-24))

    def test_prefix_zepto(self):
        prefix_tester = SIValueDimless(0)
        for prefix in ("z","zepto","Zepto"):
            self.assertEqual(prefix_tester._parse_prefix(prefix),
                             ("z",-21))

    def testprefix_atto(self):
        prefix_tester = SIValueDimless(0)
        for prefix in ("a","atto","Atto"):
            self.assertEqual(prefix_tester._parse_prefix(prefix),
                             ("a",-18))

    def test_prefix_femto(self):
        prefix_tester = SIValueDimless(0)
        for prefix in ("f","femto","Femto"):
            self.assertEqual(prefix_tester._parse_prefix(prefix),
                             ("f",-15))

    def test_prefix_pico(self):
        prefix_tester = SIValueDimless(0)
        for prefix in ("p","pico","Pico"):
            self.assertEqual(prefix_tester._parse_prefix(prefix),
                             ("p",-12))

    def test_prefix_nano(self):
        prefix_tester = SIValueDimless(0)
        for prefix in ("n","nano","Nano"):
            self.assertEqual(prefix_tester._parse_prefix(prefix),
                             ("n",-9))

    def test_prefix_micro(self):
        prefix_tester = SIValueDimless(0)
        for prefix in ("μ","micro","Micro"):
            self.assertEqual(prefix_tester._parse_prefix(prefix),
                             ("μ",-6))

    def test_prefix_milli(self):
        prefix_tester = SIValueDimless(0)
        for prefix in ("m","milli","Milli"):
            self.assertEqual(prefix_tester._parse_prefix(prefix),
                             ("m",-3))

    def test_prefix_centi(self):
        prefix_tester = SIValueDimless(0)
        for prefix in ("c","centi","Centi"):
            self.assertEqual(prefix_tester._parse_prefix(prefix),
                             ("c",-2))

    def test_prefix_deci(self):
        prefix_tester = SIValueDimless(0)
        for prefix in ("d","deci","Deci"):
            self.assertEqual(prefix_tester._parse_prefix(prefix),
                             ("d",-1))

    def test_no_prefix(self):
        prefix_tester = SIValueDimless(0)
        for prefix in ("",None):
            self.assertEqual(prefix_tester._parse_prefix(prefix),
                             ("",0))

    def test_prefix_deca(self):
        prefix_tester = SIValueDimless(0)
        for prefix in ("da","deca","Deca"):
            self.assertEqual(prefix_tester._parse_prefix(prefix),
                             ("da",1))

    def test_prefix_hecto(self):
        prefix_tester = SIValueDimless(0)
        for prefix in ("h","hecto","Hecto"):
            self.assertEqual(prefix_tester._parse_prefix(prefix),
                             ("h",2))

    def test_prefix_kilo(self):
        prefix_tester = SIValueDimless(0)
        for prefix in ("k","kilo","Kilo"):
            self.assertEqual(prefix_tester._parse_prefix(prefix),
                             ("k",3))

    def test_prefix_mega(self):
        prefix_tester = SIValueDimless(0)
        for prefix in ("M","mega","Mega"):
            self.assertEqual(prefix_tester._parse_prefix(prefix),
                             ("M",6))

    def test_prefix_giga(self):
        prefix_tester = SIValueDimless(0)
        for prefix in ("G","giga","Giga"):
            self.assertEqual(prefix_tester._parse_prefix(prefix),
                             ("G",9))

    def test_prefix_tera(self):
        prefix_tester = SIValueDimless(0)
        for prefix in ("T","tera","Tera"):
            self.assertEqual(prefix_tester._parse_prefix(prefix),
                             ("T",12))

    def test_prefix_peta(self):
        prefix_tester = SIValueDimless(0)
        for prefix in ("P","peta","Peta"):
            self.assertEqual(prefix_tester._parse_prefix(prefix),
                             ("P",15))

    def test_prefix_exa(self):
        prefix_tester = SIValueDimless(0)
        for prefix in ("E","exa","Exa"):
            self.assertEqual(prefix_tester._parse_prefix(prefix),
                             ("E",18))

    def test_prefix_zetta(self):
        prefix_tester = SIValueDimless(0)
        for prefix in ("Z","zetta","Zetta"):
            self.assertEqual(prefix_tester._parse_prefix(prefix),
                             ("Z",21))

    def test_prefix_yotta(self):
        prefix_tester = SIValueDimless(0)
        for prefix in ("Y","yotta","Yotta"):
            self.assertEqual(prefix_tester._parse_prefix(prefix),
                             ("Y",24))


class SIValueValueMethods(unittest.TestCase):
    si_v = SIValueAllPositive(1.23)
    si_v_center_kilo = SIValueAllPositiveKilo(1.23)
    si_v_prefix_kilo = SIValueAllPositive(1.23,prefix="kilo")

    # All the same
    def test_value_method(self):
        self.assertEqual(1.23, SIValueValueMethods.si_v.value())
        
    def test_si_value_method(self):
        self.assertEqual(1.23, SIValueValueMethods.si_v.si_value())

    def test_central_value_method(self):
        self.assertEqual(1.23, SIValueValueMethods.si_v.central_value())


    def test_value_method_kilo_center(self):
        self.assertEqual(1.23, SIValueValueMethods.si_v_center_kilo.value())

    def test_si_value_method_kilo_center(self):
        self.assertEqual(1.23, SIValueValueMethods.si_v_center_kilo.si_value())

    def test_central_value_method_kilo_center(self):
        self.assertEqual(1.23*10**-3, SIValueValueMethods.si_v_center_kilo.central_value())


    def test_value_method_kilo_prefix(self):
        self.assertEqual(1.23, SIValueValueMethods.si_v_prefix_kilo.value())

    def test_si_value_method_kilo_prefix(self):
        self.assertEqual(1.23, SIValueValueMethods.si_v_prefix_kilo.si_value())

    def test_central_value_method_kilo_prefix(self):
        self.assertEqual(1.23*10**3, SIValueValueMethods.si_v_prefix_kilo.central_value())


class SIValueSIUnitsMethod(unittest.TestCase):
    def test_si_units_method_all_positive(self):
        si_v = SIValueAllPositive(1.23)
        units = Units(kg=1,A=1,m=1,sec=1,cd=1,K=1,mol=1)
        self.assertEqual(si_v.si_units(),units)

    def test_si_units_method_all_negative(self):
        si_v = SIValueAllNegative(1.23)
        units = Units(kg=-1,A=-1,m=-1,sec=-1,cd=-1,K=-1,mol=-1)
        self.assertEqual(si_v.si_units(),units)

    def test_si_units_method_no_units(self):
        si_v = SIValueDimless(1.23)
        units = Units()
        self.assertEqual(si_v.si_units(),units)


class SIValueSymbols(unittest.TestCase):
    def test_symbol_method(self):
        self.assertEqual(SIValueAllPositive(1.23).symbol(),
                         "AllPos")

    def test_si_symbol_method(self):
        self.assertEqual(SIValueAllPositive(1.23).si_symbol(),
                         "AllPos")

    def test_central_symbol_method(self):
        self.assertEqual(SIValueAllPositive(1.23).central_symbol(),
                         "AllPos")


    def test_symbol_method_kilo_prefix(self):
        self.assertEqual(SIValueAllPositive(1.23,prefix="kilo").symbol(),
                         "kAllPos")

    def test_si_symbol_method_kilo_prefix(self):
        self.assertEqual(SIValueAllPositive(1.23,prefix="kilo").si_symbol(),
                         "kAllPos")

    def test_central_symbol_method_kilo_prefix(self):
        self.assertEqual(SIValueAllPositive(1.23,prefix="kilo").central_symbol(),
                         "AllPos")


    def test_symbol_method_kilo_center_prefix(self):
        self.assertEqual(SIValueAllPositiveKilo(1.23).symbol(),
                         "AllPosKilo")

    def test_si_symbol_method_kilo_center_prefix(self):
        self.assertEqual(SIValueAllPositiveKilo(1.23).si_symbol(),
                         "AllPosKilo")

    def test_central_symbol_method_kilo_center_prefix(self):
        self.assertEqual(SIValueAllPositiveKilo(1.23).central_symbol(),
                         "kAllPosKilo")


class SIValueConvertToPrefix(unittest.TestCase):
    def test_convert_to_prefix_micro_check_value(self):
        self.assertEqual(SIValueAllPositive(1.23).convert_to_prefix("μ").value(),
                         1.23*10**6)

    def test_convert_to_prefix_micro_check_symbol(self):
        self.assertEqual(SIValueAllPositive(1.23).convert_to_prefix("μ").symbol(),
                         "μAllPos")

    def test_convert_to_prefix_tera_check_value(self):
        self.assertEqual(SIValueAllPositive(1.23).convert_to_prefix("T").value(),
                         1.23*10**-12)

    def test_convert_to_prefix_tera_check_symbol(self):
        self.assertEqual(SIValueAllPositive(1.23).convert_to_prefix("T").symbol(),
                         "TAllPos")


class SIValueConvertToUnit(unittest.TestCase):
    def test_convert_to_self(self):
        si_v = SIValueAllPositive(1.23)
        self.assertIs(si_v,si_v.convert_to_unit('AllPos'))

    def test_convert_to_other(self):
        si_v = SIValueAllPositive(1.23)
        with self.assertRaises(ValueError):
            si_v.convert_to_unit("<invalid>")


class SIValueStrReprMethods(unittest.TestCase):
    def test_str(self):
        self.assertEqual(str(SIValueAllPositive(1.23)),
                         "{} {}".format(1.23,"AllPos"))

    def test_repr(self):
        self.assertEqual(SIValueAllPositive(1.23).__repr__(),
                         "{} {}".format(1.23,"AllPos"))