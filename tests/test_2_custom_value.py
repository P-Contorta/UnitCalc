import unittest

from unitcalc.value_types.value import CustomValue

# Things to test
# cls.is_value() returns false
# __init__()
# self.value()
# self.si_value()
# self.central_value()
# self.symbol()
# self.si_symbol()
# self.si_units
# self.__str__
# self.__repr__

# add / subtract

# mult / divide

# power

# eq / ne
# gt / le
# lt / ge

class CustomValueIsValueMethod(unittest.TestCase):
    def test_is_value(self):
        test_names = ("kg, Kilogram, meter, Celcius, Pound, cd, mol, Amps")
        for name in test_names:
            self.assertFalse(CustomValue.is_value(name))