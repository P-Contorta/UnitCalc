# UnitCalc
A Python Library for doing Scientific/Engineering mathematics! 

This library explicity supports the following SI units:

Base Units:
- Ampere
- Candela
- Kilogram
- Meter
- Mol
- Kelvin
- Second

Compound/Complex Units:
- Newton
- Ohm
- Coulomb
- Volt
- Watt
- Joule
- Pascal

Non Si Units:
- Pound/lb
- Ton
- Inch
- Foot
- Mile
- Celcius
- Fahrenheit
- Minute
- Hour

Values can be created with units not explicitly supported by the above units but they will be represented as combination of the 7 base SI units.

## Installation:
clone this repository to your machine then execute the following:
```
pip install <path/to/UnitCalc/>
```

## Upgrade:
pull the latest version from the main branch then execute the following:
```
pip install <path/to/UnitCalc/> --upgrade
```

## Usage:
### 1.) Getting Started:
```python
>>> from unitcalc import Physics
>>>
>>> # Create a factory object
>>> physics = Physics()
>>>
>>> # Create an Ampere Unit
>>> A = physics.create(13,"A")
>>> A
13 A
>>> # Create a Dimensionless Unit
>>> no_dim = physics.create(1)
>>> no_dim
1
```

### 2.) Creating values with custom units
```python
>>> from unitcalc import Physics
>>> from units import Units
>>> physics = Physics()
>>> # Unit accepts the 7 base SI units as key-word arguments
>>> # A-> Ampere
>>> # K-> Kelvin
>>> # sec -> second
>>> # m -> meter
>>> # kg -> kilogram
>>> # cd -> candela
>>> # mol -> Mol
>>> # Webber kg⋅m2⋅s−2⋅A−1
>>> webber = physics.create(1.34,Units(kg=1,m=2,sec=-2,A=-1))
>>> webber
1.34 m² kg / sec² A 
```

### 3.) Creating SI units with different scales
```python
>>> from unitcalc import Physics
>>> physics = Physics()
>>>
>>> # Create a nanoAmpere
>>> nA = physics.create(13,"A",unit_prefix="nano")
>>> nA
13 nA
>>> # Convert 13nA to Ampere
>>> # Passing None or "" will return an un-prefixed value
>>> A = nA.convert_to_prefix(None)
>>> A
1.3e-08 A
```

### 4.) Converting between SI and Non-SI units
```python
>>> from unitcalc import Physics
>>> physics = Physics()
>>> 
>>> C = physics.create(0,"C")
>>> F = C.convert_to_unit("F")
>>> K = F.convert_to_unit("K")
>>> C
0 ⁰C
>>> F
32.0 ⁰F
>>> K
273.15 K
```

### 5.) Maths and conversions
#### a.) Doubling Temperature
```python
>>> from unitcalc import Physics
>>> physics = Physics()
>>>
>>> # Double the temperature at 0 oC
>>> C = physics.create(0,"C")
>>> double_C = C*2
>>> C
0 ⁰C
>>> double_C
273.15 ⁰C
```
#### b.) Addition/Subtraction
```python
>>> from unitcalc import Physics
>>> physics = Physics()
>>>
>>> inch = physics.create(12,"In")
>>> foot = physics.create(1,"ft")
>>> inch + foot
24 in
>>> foot + inch
2 ft
>>> kg = physics.create(1.2,"kg")
>>> foot + kg
ValueError: Cannot perform addition because the units do not match.
```
#### c.) Powers
```python
>>> from unitcalc import Physics
>>> physics = Physics()
>>>
>>> mm = physics.create(1,"meter",unit_prefix="mili")
>>> mm**2
1e-06 m²
```

### 6.) Boolean Operations
```python
>>> from unitcalc import Physics
>>> physics = Physics()
>>>
>>> inch = physics.create(12,"In")
>>> foot = physics.create(1,"ft")
>>> inch == foot
True
```

### 7.) Constants
```python
>>> from unitcalc import Constants
>>> # All Constants
>>> Constants
Constants:
Boltzmann:                    1.380649e-23 m² kg / sec² K 
G:                            6.6743015e-11 m³ / sec² kg 
N0:                           6.02214076e+23 
Na:                           6.02214076e-23 / mol 
Planck:                       6.62607015e-34 m² kg / sec 
R:                            8.31446261815324 m² kg / sec² K mol 
Rydberg_h:                    10967758.329787835 / m 
Rydberg_inf:                  10973731.557661768 / m 
Stefan:                       5.6703744191844294e-08 kg / sec³ K⁴ 
Stefan_Boltzmann:             5.6703744191844294e-08 kg / sec³ K⁴ 
Wiens:                        0.002897771955 m K 
alpha:                        0.007297352565816523 
avogadro_constant:            6.02214076e-23 / mol 
avogadro_number:              6.02214076e+23 
c:                            299792458 m / sec 
e:                            1.6021766340000001e-19 C
electron_rest_mass:           9.1093837015e-31 kg
elementary_charge:            1.6021766340000001e-19 C
epsilon_0:                    8.854187816999999e-12 sec⁴ A² / m³ kg 
fine_structure:               0.007297352565816523 
g:                            9.80665 m / sec² 
gas_constant:                 8.31446261815324 m² kg / sec² K mol 
gravitational_constant:       6.6743015e-11 m³ / sec² kg 
h:                            6.62607015e-34 m² kg / sec 
hbar:                         1.0545718176461565e-34 m² kg / sec 
k:                            1.380649e-23 m² kg / sec² K 
m_e:                          9.1093837015e-31 kg
m_n:                          1.67492749804e-27 kg
m_p:                          1.67262192369e-27 kg
mu_0:                         1.25e-08 m kg / sec² A² 
neutron_rest_mass:            1.67492749804e-27 kg
proton_rest_mass:             1.67262192369e-27 kg
rydberg_h_constant:           10967758.329787835 / m 
rydberg_inf_constant:         10973731.557661768 / m 
sigma:                        5.6703744191844294e-08 kg / sec³ K⁴ 
speed_of_light:               299792458 m / sec 
standard_gravity:             9.80665 m / sec² 
wiens_displacement_constant:  0.002897771955 m K
>>>
>>> # Speed of light
>>> Constants.speed_of_light()
299792458 m / sec
>>> Constants.c()
299792458 m / sec
```
