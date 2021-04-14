from .parse_units import SIUnitParser
from ..value_types.complex_values.electric_potential import Volt
from ..value_types.complex_values.power import Watt
from ..value_types.complex_values.electric_resistance import Ohm

class ElectricianParser(SIUnitParser):
    def __init__(self):
        super().__init__(Ohm, Volt, Watt)