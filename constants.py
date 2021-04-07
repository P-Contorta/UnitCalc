from physics import PhysObjects
from units import Units

import math

class _MetaConstants(type):
    def __repr__(cls):
        print_str = "Constants:\n"
        for cls_meth in dir(cls):
            if not cls_meth.startswith("__") and not cls_meth.endswith("__"):
                if callable(getattr(cls, cls_meth)):
                    print_str += "{}:{}{}\n".format(cls_meth,
                                                    " " * (29 - len(cls_meth)),
                                                    getattr(cls, cls_meth)())

        return print_str


class Constants(metaclass=_MetaConstants):
    Phys = PhysObjects()

    @classmethod
    def c(cls):
        return cls.Phys.create(299792458,Units(m=1,sec=-1))

    @classmethod
    def speed_of_light(cls):
        return cls.c()


    @classmethod
    def mu_0(cls):
        # approximate value
        return cls.Phys.create(1.25 * 10**-8, Units(kg=1,m=1,sec=-2,A=-2))

    @classmethod
    def epsilon_0(cls):
        return cls.Phys.create(8.854187817 * 10**-12, Units(sec=4,A=2,kg=-1,m=-3))

    @classmethod
    def h(cls):
        return cls.Phys.create(6.62607015 * 10**-34, Units(kg=1,m=2,sec=-1))
    
    @classmethod
    def Planck(cls):
        return cls.h()

    @classmethod
    def hbar(cls):
        return cls.h()/(2*math.pi)

    
    @classmethod
    def G(cls):
        return cls.Phys.create(6.6743015 * 10**-11, Units(m=3,kg=-1,sec=-2))

    @classmethod
    def gravitational_constant(cls):
        return cls.G()


    @classmethod
    def g(cls):
        return cls.Phys.create(9.80665, Units(m=1,sec=-2))

    @classmethod
    def standard_gravity(cls):
        return cls.g()


    @classmethod
    def e(cls):
        return cls.Phys.create(1.602176634 * 10**-19, unit="Coulomb")

    @classmethod
    def elementary_charge(cls):
        return cls.e()


    @classmethod
    def R(cls):
        return cls.Phys.create(8.31446261815324,Units(kg=1,m=2,K=-1,mol=-1,sec=-2))
    
    @classmethod
    def gas_constant(cls):
        return cls.R()

    
    @classmethod
    def alpha(cls):
        return (cls.Phys.create(1) / (cls.epsilon_0() * 4 * math.pi)) * (cls.e()**2 / (cls.hbar()*cls.c()))

    @classmethod
    def fine_structure(cls):
        return cls.alpha()


    @classmethod
    def Na(cls):
        return cls.Phys.create(6.02214076 * 10**-23,Units(mol=-1))

    @classmethod
    def avogadro_constant(cls):
        return cls.Na()

    @classmethod
    def N0(cls):
        return cls.Phys.create(6.02214076 * 10**23)

    @classmethod
    def avogadro_number(cls):
        return cls.N0()


    @classmethod
    def k(cls):
        return cls.Phys.create(1.380649 * 10**-23,Units(kg=1,m=2,sec=-2,K=-1))

    @classmethod
    def Boltzmann(cls):
        return cls.k()


    @classmethod
    def sigma(cls):
        return (cls.k()**4 * math.pi**2) / (cls.hbar()**3 * cls.c()**2 * 60)

    @classmethod
    def Stefan_Boltzmann(cls):
        return cls.sigma()

    @classmethod
    def Stefan(cls):
        return cls.sigma()


    @classmethod
    def Wiens(cls):
        return cls.Phys.create(0.002897771955,Units(m=1,K=1))

    @classmethod
    def wiens_displacement_constant(cls):
        return cls.Wiens()


    @classmethod
    def m_e(cls):
        return cls.Phys.create(9.1093837015 * 10**-31,unit="kg")

    @classmethod
    def electron_rest_mass(cls):
        return cls.m_e()

    
    @classmethod
    def m_p(cls):
        return cls.Phys.create(1.67262192369 * 10**-27,unit="kg")

    @classmethod
    def proton_rest_mass(cls):
        return cls.m_p()


    @classmethod
    def m_n(cls):
        return cls.Phys.create(1.67492749804 * 10**-27,unit="kg")

    @classmethod
    def neutron_rest_mass(cls):
        return cls.m_n()



    @classmethod
    def Rydberg_inf(cls):
        return (cls.m_e() * cls.e()**4) / (cls.h()**3 * cls.c() * cls.epsilon_0()**2 * 8)

    @classmethod
    def rydberg_inf_constant(cls):
        return cls.Rydberg_inf()

    @classmethod
    def Rydberg_h(cls):
        return cls.Rydberg_inf() * (cls.m_p()/ (cls.m_e() + cls.m_p()))

    @classmethod
    def rydberg_h_constant(cls):
        return cls.Rydberg_h()