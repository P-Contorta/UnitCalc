from .value_types import value_types_container
from .value_types.value import SIValue, NonSIValue, CustomValue
from .units import Units

from typing import TypeVar

# Types
number_type = TypeVar("number",int,float)
unit_type = TypeVar("unit",str,Units,None)
class Physics(object):
    def create(self,value:number_type, unit:unit_type=None, unit_prefix:str=-1):
        if not isinstance(value,(int,float)):
            raise TypeError("Values must have the type float or int.")
        
        if isinstance(unit,str):
            found_value = False
            for value_type in value_types_container:
                if value_type.is_value(unit):
                    found_value = True
                    if issubclass(value_type,SIValue):
                        if unit_prefix != -1:
                            return value_type(value,prefix=unit_prefix)
                        else:
                            return value_type(value)
                    else:
                        return value_type(value)
                    break

            if not found_value:
                msg = "The unit '{}' is not a supported measurement.".format(unit)
                raise AttributeError(msg)

        elif isinstance(unit,Units):
            return CustomValue(value,**unit.as_dict())
        elif unit is None:
            return CustomValue(value)
        else:
            raise AttributeError("The unit provided must be a string, None, or of type Units()")