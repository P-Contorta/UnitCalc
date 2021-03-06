from ..value import SIValue
from ..value import NonSIValue


class Meter(SIValue):
    _re_pattern = "^[Mm]$|^[Mm]eters?$"

    def __init__(self,value,prefix:str=""):
        super().__init__(value,prefix=prefix,m=1)

    def _base_symbol(self):
        return "m"

    def convert_to_unit(self,unit_name:str):
        if Inch.is_value(unit_name):
            return Inch(self.central_value() * 39.370078740157)
        elif Foot.is_value(unit_name):
            return Foot(self.central_value() * 3.2808398950131)
        elif Mile.is_value(unit_name):
            return Mile(self.central_value() * 3.2808398950131/ 5280)
        elif Meter.is_value(unit_name):
            return self
        else:
            raise ValueError("Cannot convert to {}.".format(unit_name))


class Inch(NonSIValue):
    _re_pattern = "^[Ii]n(ches)?$|^[Ii]nch$"

    def __init__(self,value):
        super().__init__(value,Meter(value * 0.0254),m=1)

    def _base_symbol(self):
        return "in"


class Foot(NonSIValue):
    _re_pattern = "^[Ff](oo)?t$|^[Ff]eet$"

    def __init__(self,value):
        super().__init__(value,Meter(value * 0.3048),m=1)

    def _base_symbol(self):
        return "ft"


class Mile(NonSIValue):
    _re_pattern = "^[Mm]i(le)?$|^[Mm]iles?$"
    
    def __init__(self,value):
        super().__init__(value,Meter(value * 5280/3.2808398950131),m=1)

    def _base_symbol(self):
        return "Mi"