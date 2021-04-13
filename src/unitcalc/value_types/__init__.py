from .base_values.current import Ampere
from .base_values.distance import Meter, Inch, Foot, Mile
from .base_values.luminosity import Candela
from .base_values.mass import Kilogram, Pound, Ton
from .base_values.substance import Mol
from .base_values.temperature import Kelvin, Celcius, Fahrenheit
from .base_values.time import Second, Minute, Hour


from .complex_values.energy import Joule
from .complex_values.charge import Coulomb
from .complex_values.power import Watt
from .complex_values.electric_potential import Volt
from .complex_values.electric_resistance import Ohm
from .complex_values.force import Newton
from .complex_values.pressure import Pascal


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