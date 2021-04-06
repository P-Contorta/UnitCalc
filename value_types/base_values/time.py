from value_types.value import SIValue
from value_types.value import NonSIValue

class Second(SIValue):
    _re_pattern = "[Ss]ec(ond)?s?$"

    def __init__(self,value,prefix:str=""):
        super().__init__(value,prefix=prefix,sec=1)

    def _base_symbol(self):
        return "sec"

    def convert_to_unit(self,unit_name:str):
        if Minute.is_value(unit_name):
            return Minute(self.central_value() / 60)
        elif Hour.is_value(unit_name):
            return Hour(self.central_value() / 3600)
        elif Second.is_value(unit_name):
            return self
        else:
            raise ValueError("Cannot convert to {}.".format(unit_name))


class Minute(NonSIValue):
    _re_pattern = "^[Mm]in(ute)?s?$"

    def __init__(self,value):
        super().__init__(value,Second(value * 60),sec=1)

    def _base_symbol(self):
        return "min"


class Hour(NonSIValue):
    _re_pattern = "^[Hh](ou)?rs?$"

    def __init__(self,value):
        super().__init__(value,Second(value * 3600),sec=1)

    def _base_symbol(self):
        return "hr"
