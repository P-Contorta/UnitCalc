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


## Usage:
### 1.) Getting Started:
```python
>>> from physics import PhysObjects
>>>
>>> # Create a factory object
>>> phys_factory = PhysObjects()
>>>
>>> # Create an Ampere Unit
>>> A = phys_factory.create(13,"A")
>>> A
13 A
>>> # Create a Dimensionless Unit
>>> no_dim = phys_factory.create(1)
>>> no_dim
1
```

### 2.) Creating SI units with different scales
```python
>>> from physics import PhysObjects
>>> phys_factory = PhysObjects()
>>>
>>> # Create a nanoAmpere
>>> nA = phys_factory.create(13,"A",unit_prefix="nano")
>>> nA
13 nA
>>> # Convert 13nA to Ampere
>>> # Passing None or "" will return an un-prefixed value
>>> A = nA.convert_to_prefix(None)
>>> A
1.3e-08 A
```

### 3.) Converting between SI and Non-SI units
```python
>>> from physics import PhysObjects
>>> phys_factory = PhysObjects()
>>> 
>>> C = phys_factory.create(0,"C")
>>> F = C.convert_to_unit("F")
>>> K = F.convert_to_unit("K")
>>> C
0 C
>>> F
32.0 F
>>> K
273.15 K
```

### 4.) Maths and conversions
#### a.) Doubling Temperature
```python
>>> from physics import PhysObjects
>>> phys_factory = PhysObjects()
>>>
>>> # Double the temperature at 0 oC
>>> C = phys_factory.create(0,"C")
>>> double_C = C*2
>>> C
0 C
>>> double_C
273.15 C
```
#### b.) Addition/Subtraction
```python
>>> from physics import PhysObjects
>>> phys_factory = PhysObjects()
>>>
>>> inch = phys_factory.create(12,"In")
>>> foot = phys_factory.create(1,"ft")
>>> inch + foot
24 in
>>> foot + inch
2 ft
>>> kg = phys_factory.create(1.2,"kg")
>>> foot + kg
ValueError: Cannot perform addition because the units do not match.
```
#### c.) Powers
```python
>>> from physics import PhysObjects
>>> phys_factory = PhysObjects()
>>>
>>> mm = phys_factory.create(1,"meter",unit_prefix="mili")
>>> mm**2
1e-06 m²
```

### 5.) Boolean Operations
```python
>>> from physics import PhysObjects
>>> phys_factory = PhysObjects()
>>>
>>> inch = phys_factory.create(12,"In")
>>> foot = phys_factory.create(1,"ft")
>>> inch == foot
True
```

### 6.) Constants
```python
>>> from constants import Constants
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
