from ..value import SIValue
from ..value import NonSIValue

class Kilogram(SIValue):
    _re_pattern = "g$|[Gg]rams?$"

    def __init__(self,value,prefix:str="kilo",parser=None):
        super().__init__(value,
                         prefix=prefix,center_prefix="kilo",
                         kg=1,
                         parser=parser)

    def _base_symbol(self):
        return "g"
    
    def convert_to_unit(self,unit_name:str):
        if Pound.is_value(unit_name):
            return Pound(self.central_value() * 2.2046226218)
        elif Ton.is_value(unit_name):
            return Ton(self.central_value() * 2.2046226218/2000)
        elif Kilogram.is_value(unit_name):
            return self
        else:
            raise ValueError("Cannot convert to {}.".format(unit_name))



class Pound(NonSIValue):
    _re_pattern = "^[Ll]bs?$|^[Pp]ounds?$"

    def __init__(self,value):
        super().__init__(value,
                         Kilogram(value / 2.2046226218),
                         kg=1,
                         parser=parser)

    def _base_symbol(self):
        return "lb"



class Ton(NonSIValue):
    _re_pattern = "^[Tt]ons?$"

    def __init__(self,value):
        super().__init__(value,
                         Kilogram(value * 2000/2.2046226218),
                         kg=1,
                         parser=parser)

    def _base_symbol(self):
        return "ton"