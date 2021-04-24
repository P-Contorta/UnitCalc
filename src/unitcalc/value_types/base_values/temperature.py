from ..value import SIValue
from ..value import NonSIValue

class Kelvin(SIValue):
    _re_pattern = "^K$|^[Kk](elvin)?$"

    def __init__(self,value,prefix:str="kilo",parser=None):
        super().__init__(value,
                         prefix=prefix,
                         K=1,
                         parser=parser)

    def _base_symbol(self):
        return "K"
        
    def convert_to_unit(self,unit_name:str):
        if Fahrenheit.is_value(unit_name):
            return Fahrenheit(((self.central_value() - 273.15) * 1.8) + 32)
        elif Celcius.is_value(unit_name):
            return Celcius(self.central_value() - 273.15)
        elif Kelvin.is_value(unit_name):
            return self
        else:
            raise ValueError("Cannot convert to {}.".format(unit_name))


class Celcius(NonSIValue):
    _re_pattern = "^⁰C$|^[Cc](elcius)?$"

    def __init__(self,value,parser=None):
        super().__init__(value,
                         Kelvin(value + 273.15),
                         K=1,
                         parser=parser)

    def _base_symbol(self):
        return "⁰C"
        

class Fahrenheit(NonSIValue):
    _re_pattern = "^⁰F$|^[Ff](ahrenheit)?$"

    def __init__(self,value,parser=None):
        super().__init__(value,
                         Kelvin(((value - 32) / 1.8) + 273.15),
                         K=1,
                         parser=parser)

    def _base_symbol(self):
        return "⁰F"
