from .parse_units import SIUnitParser
from ..value_types.complex_values.force import Newton
from ..value_types.complex_values.energy import Joule
from ..value_types.complex_values.pressure import Pascal

class PhysicsParser(SIUnitParser):
    def __init__(self):
        super().__init__(Newton, Joule, Pascal)