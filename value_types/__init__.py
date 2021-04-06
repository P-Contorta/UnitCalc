from value_types.base_values.current import Ampere
from value_types.base_values.distance import Meter, Inch, Foot, Mile
from value_types.base_values.luminosity import Candela
from value_types.base_values.mass import Kilogram, Pound, Ton
from value_types.base_values.substance import Mol
from value_types.base_values.temperature import Kelvin, Celcius, Fahrenheit
from value_types.base_values.time import Second, Minute, Hour


from value_types.complex_values.energy import Joule
from value_types.complex_values.charge import Coulomb
from value_types.complex_values.power import Watt
from value_types.complex_values.electric_potential import Volt
from value_types.complex_values.electric_resistance import Ohm
from value_types.complex_values.force import Newton
from value_types.complex_values.pressure import Pascal


value_types_container = (Joule,
                         Coulomb,
                         Watt,
                         Volt,
                         Ohm,
                         Newton,
                         Pascal,
                         Second, Minute, Hour,
                         Meter, Inch, Foot, Mile,
                         Kilogram, Pound, Ton,
                         Kelvin, Celcius, Fahrenheit,
                         Ampere,
                         Candela,
                         Mol)