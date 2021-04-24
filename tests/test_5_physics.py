import unittest
from unitcalc import Physics
from unitcalc import Units

from unitcalc.value_types.value import CustomValue
from unitcalc.value_types.base_values.current import Ampere
from unitcalc.value_types.base_values.distance import Meter, Inch, Foot, Mile
from unitcalc.value_types.base_values.luminosity import Candela
from unitcalc.value_types.base_values.mass import Kilogram, Pound, Ton
from unitcalc.value_types.base_values.substance import Mol
from unitcalc.value_types.base_values.temperature import Kelvin, Celcius, Fahrenheit
from unitcalc.value_types.base_values.time import Second, Minute, Hour

from unitcalc.value_types.complex_values.energy import Joule
from unitcalc.value_types.complex_values.charge import Coulomb
from unitcalc.value_types.complex_values.power import Watt
from unitcalc.value_types.complex_values.electric_potential import Volt
from unitcalc.value_types.complex_values.electric_resistance import Ohm
from unitcalc.value_types.complex_values.force import Newton
from unitcalc.value_types.complex_values.pressure import Pascal

class PhysicsInit(unittest.TestCase):
    def test_init(self):
        self.assertIsInstance(Physics(),Physics)


class PhysicsCreateValue(unittest.TestCase):
    def test_int_value_dimless(self):
        ans = CustomValue(2)
        self.assertEqual(ans,Physics().create(2))

    def test_float_value_dimless(self):
        ans = CustomValue(2.1)
        self.assertEqual(ans,Physics().create(2.1))

    def test_invalid_value_dimless(self):
        with self.assertRaises(TypeError):
            Physics().create("invalid")


class PhysicsCreateUnitType(unittest.TestCase):
    def test_dimless(self):
        ans = CustomValue(2.3)
        self.assertEqual(ans,Physics().create(2.3))

    def test_custom_units(self):
        ans = CustomValue(2.3,kg=1,A=-2,m=3)
        self.assertEqual(ans,Physics().create(2.3,Units(kg=1,A=-2,m=3)))

    def test_invalid_type(self):
        with self.assertRaises(AttributeError):
            Physics().create(1,[])

    def test_str_not_found(self):
        unit_str = "invalid"
        with self.assertRaisesRegex(AttributeError,
                                    "The unit '{}' is not a supported measurement\."\
                                    .format(unit_str)):
            Physics().create(1,unit_str)
                                    

class ValueTypes(unittest.TestCase):
    def test_create_ampere(self):
        physics = Physics()
        unit = Ampere(1)
        for unit_str in ("A","Amp","amp","Amps","amps","Ampere","Amperes"):
            self.assertEqual(unit,physics.create(1,unit_str))

    def test_create_meter(self):
        physics = Physics()
        unit = Meter(1)
        for unit_str in ("M","m", "Meter", "Meters", "meter", "meters"):
            self.assertEqual(unit,physics.create(1,unit_str))

    def test_create_inch(self):
        physics = Physics()
        unit = Inch(1)
        for unit_str in ("In", "in", "Inch", "inch", "Inches", "inches"):
            self.assertEqual(unit,physics.create(1,unit_str))

    def test_create_foot(self):
        physics = Physics()
        unit = Foot(1)
        for unit_str in ("Ft", "ft", "Foot", "foot", "Feet", "feet"):
            self.assertEqual(unit,physics.create(1,unit_str))

    def test_create_mile(self):
        physics = Physics()
        unit = Mile(1)
        for unit_str in ("Mi", "mi", "Mile", "mile", "Miles", "miles"):
            self.assertEqual(unit,physics.create(1,unit_str))

    def test_create_candela(self):
        physics = Physics()
        unit = Candela(1)
        for unit_str in ("cd", "Candela", "candela", "Candelas","candelas"):
            self.assertEqual(unit,physics.create(1,unit_str))

    def test_create_kilogram(self):
        physics = Physics()
        unit = Kilogram(1)
        for unit_str in ("Kg", "kg", "Kilogram", "kilogram", "Kilograms", "kilograms"):
            self.assertEqual(unit,physics.create(1,unit_str))

    def test_create_pound(self):
        physics = Physics()
        unit = Pound(1)
        for unit_str in ("Lb", "lb", "Pound", "pound", "Pounds", "pounds"):
            self.assertEqual(unit,physics.create(1,unit_str))

    def test_create_ton(self):
        physics = Physics()
        unit = Ton(1)
        for unit_str in ("Ton", "ton", "Tons", "tons"):
            self.assertEqual(unit,physics.create(1,unit_str))

    def test_create_mol(self):
        physics = Physics()
        unit = Mol(1)
        for unit_str in ("Mol", "mol", "Mols", "mols"):
            self.assertEqual(unit,physics.create(1,unit_str))

    def test_create_kelvin(self):
        physics = Physics()
        unit = Kelvin(1)
        for unit_str in ("K", "k", "Kelvin", "kelvin"):
            self.assertEqual(unit,physics.create(1,unit_str))

    def test_create_celcius(self):
        physics = Physics()
        unit = Celcius(1)
        for unit_str in ("⁰C", "C", "c", "Celcius", "celcius"):
            self.assertEqual(unit,physics.create(1,unit_str))

    def test_create_fahrenheit(self):
        physics = Physics()
        unit = Fahrenheit(1)
        for unit_str in ("⁰F", "F", "f", "Fahrenheit", "fahrenheit"):
            self.assertEqual(unit,physics.create(1,unit_str))

    def test_create_second(self):
        physics = Physics()
        unit = Second(1)
        for unit_str in ("Sec", "sec", "Second", "second", "Seconds", "Seconds"):
            self.assertEqual(unit,physics.create(1,unit_str))

    def test_create_minute(self):
        physics = Physics()
        unit = Minute(1)
        for unit_str in ("Min", "min", "Minute", "minute", "Minutes" , "Minutes"):
            self.assertEqual(unit,physics.create(1,unit_str))

    def test_create_hour(self):
        physics = Physics()
        unit = Hour(1)
        for unit_str in ("Hr", "hr", "Hour", "hour", "Hours", "hours"):
            self.assertEqual(unit,physics.create(1,unit_str))

    def test_create_coulomb(self):
        physics = Physics()
        unit = Coulomb(1)
        for unit_str in ("Coul", "coul", "Coulomb", "coulomb", "Coulombs", "coulombs"):
            self.assertEqual(unit,physics.create(1,unit_str))

    def test_create_volt(self):
        physics = Physics()
        unit = Volt(1)
        for unit_str in ("V", "v", "Volt", "volt", "Volts", "volts"):
            self.assertEqual(unit,physics.create(1,unit_str))

    def test_create_ohm(self):
        physics = Physics()
        unit = Ohm(1)
        for unit_str in ( "Ω", "Ohm", "ohm"):
            self.assertEqual(unit,physics.create(1,unit_str))

    def test_create_joule(self):
        physics = Physics()
        unit = Joule(1)
        for unit_str in ("J", "Joule", "joule", "Joules", "joules"):
            self.assertEqual(unit,physics.create(1,unit_str))

    def test_create_newton(self):
        physics = Physics()
        unit = Newton(1)
        for unit_str in ("N", "Newton", "newton", "Newtons", "newtons"):
            self.assertEqual(unit,physics.create(1,unit_str))

    def test_create_watt(self):
        physics = Physics()
        unit = Watt(1)
        for unit_str in ("W", "Watt", "watt", "Watts", "watts"):
            self.assertEqual(unit,physics.create(1,unit_str))

    def test_create_pascal(self):
        physics = Physics()
        unit = Pascal(1)
        for unit_str in ("Pa", "Pascal", "pascal", "Pascals", "pascals"):
            self.assertEqual(unit,physics.create(1,unit_str))