import unittest
from unitcalc import Physics
from unitcalc import Units
from unitcalc import Constants

import math


class ConstantsSpeedOfLight(unittest.TestCase):
    def test_c(self):
        c = Physics().create(299792458,Units(m=1,sec=-1))
        self.assertEqual(Constants.c(),c)

    def test_speed_of_light(self):
        self.assertEqual(Constants.c(),Constants.speed_of_light())

class ConstantsMu0(unittest.TestCase):
    def test_mu0(self):
        mu_0 = Physics().create(1.25 * 10**-8, Units(kg=1,m=1,sec=-2,A=-2))
        self.assertEqual(Constants.mu_0(),mu_0)

class ConstantsEpsilon0(unittest.TestCase):
    def epsilon_0(self):
        epsilon_0 = Physics().create(8.854187817 * 10**-12, Units(sec=4,A=2,kg=-1,m=-3))
        self.assertEqual(Constants.epsilon_0(),epsilon_0)

class ConstantsPanckConstant(unittest.TestCase):
    def test_h(self):
        h = Physics().create(6.62607015 * 10**-34, Units(kg=1,m=2,sec=-1))
        self.assertEqual(Constants.h(),h)

    def test_planck(self):
        self.assertEqual(Constants.h(),Constants.Planck())

    def test_hbar(self):
        self.assertEqual(Constants.h()/(2*math.pi),Constants.hbar())

class ConstantsGraviationConstant(unittest.TestCase):
    def test_G(self):
        G = Physics().create(6.6743015 * 10**-11, Units(m=3,kg=-1,sec=-2))
        self.assertEqual(Constants.G(),G)

    def test_gravitation_constant(self):
        self.assertEqual(Constants.G(),Constants.gravitational_constant())

class ConstantsStandardGravity(unittest.TestCase):
    def test_g(self):
        g = Physics().create(9.80665, Units(m=1,sec=-2))
        self.assertEqual(Constants.g(),g)

    def test_standard_gravity(self):
        self.assertEqual(Constants.standard_gravity(),Constants.g())

class ConstantsElementaryCharge(unittest.TestCase):
    def test_e(self):
        e = Physics().create(1.602176634 * 10**-19, unit="Coulomb")
        self.assertEqual(Constants.e(),e)

    def test_elementary_charge(self):
        self.assertEqual(Constants.elementary_charge(),Constants.e())

class ConstantsGasConstant(unittest.TestCase):
    def test_R(self):
        R = Physics().create(8.31446261815324,Units(kg=1,m=2,K=-1,mol=-1,sec=-2))
        self.assertEqual(Constants.R(),R)

    def test_gas_constant(self):
        self.assertEqual(Constants.R(),Constants.gas_constant())

class ConstantsFineStructure(unittest.TestCase):
    def test_alpha(self):
        epsilon_0 = Constants.epsilon_0()
        e = Constants.e()
        hbar = Constants.hbar()
        c = Constants.c()
        alpha = (e**2 / (hbar*c)) / (epsilon_0 * 4 * math.pi)
        self.assertEqual(Constants.alpha(),alpha)

    def test_fine_structure(self):
        self.assertEqual(Constants.alpha(),Constants.fine_structure())

class ConstantsAvogadroConstant(unittest.TestCase):
    def test_Na(self):
        Na = Physics().create(6.02214076 * 10**-23,Units(mol=-1))
        self.assertEqual(Constants.Na(),Na)

    def test_avogadro_constant(self):
        self.assertEqual(Constants.Na(),Constants.avogadro_constant())

class ConstantsAvogadroNumber(unittest.TestCase):
    def test_N0(self):
        N0 = Physics().create(6.02214076 * 10**23)
        self.assertEqual(Constants.N0(),N0)

    def test_avogadro_number(self):
        self.assertEqual(Constants.N0(),Constants.avogadro_number())

class ConstantsBoltzmann(unittest.TestCase):
    def test_k(self):
        k = Physics().create(1.380649 * 10**-23,Units(kg=1,m=2,sec=-2,K=-1))
        self.assertEqual(Constants.k(),k)

    def test_boltzmann(self):
        self.assertEqual(Constants.k(),Constants.Boltzmann())

class ConstantsStefanBoltzmann(unittest.TestCase):
    def test_sigma(self):
        k = Constants.k()
        hbar = Constants.hbar()
        c = Constants.c()
        sigma = (k**4 * math.pi**2) / (hbar**3 * c**2 * 60)
        self.assertEqual(Constants.sigma(),sigma)

    def test_stefan_boltzmann(self):
        self.assertEqual(Constants.sigma(),Constants.Stefan_Boltzmann())

    def test_stefan(self):
        self.assertEqual(Constants.sigma(),Constants.Stefan())

class ConstantsWiensDisiplaement(unittest.TestCase):
    def test_wiens(self):
        weins = Physics().create(0.002897771955,Units(m=1,K=1))
        self.assertEqual(Constants.Wiens(),weins)

    def test_wiens_displacement_constant(self):
        self.assertEqual(Constants.Wiens(),Constants.wiens_displacement_constant())

class ConstantsElectronRestMass(unittest.TestCase):
    def test_m_e(self):
        m_e = Physics().create(9.1093837015 * 10**-31,unit="kg")
        self.assertEqual(Constants.m_e(),m_e)

    def test_electron_rest_mass(self):
        self.assertEqual(Constants.m_e(),Constants.electron_rest_mass())

class ConstantsProtonRestMass(unittest.TestCase):
    def test_m_p(self):
        m_p = Physics().create(1.67262192369 * 10**-27,unit="kg")
        self.assertEqual(Constants.m_p(),m_p)

    def test_proton_rest_mass(self):
        self.assertEqual(Constants.m_p(),Constants.proton_rest_mass())

class ConstantsNeutronRestMass(unittest.TestCase):
    def test_m_n(self):
        m_n = Physics().create(1.67492749804 * 10**-27,unit="kg")
        self.assertEqual(Constants.m_n(),m_n)

    def test_neutron_rest_mass(self):
        self.assertEqual(Constants.m_n(),Constants.neutron_rest_mass())

class ConstantsRydbergInf(unittest.TestCase):
    def test_rydberg_inf(self):
        m_e = Constants.m_e()
        e = Constants.e()
        h = Constants.h()
        c = Constants.c()
        epsilon_0 = Constants.epsilon_0()
        rydberg_inf = (m_e * e**4) / (h**3 * c * epsilon_0**2 * 8)
        self.assertEqual(Constants.Rydberg_inf(),rydberg_inf)

    def test_rydberg_inf_constant(self):
        self.assertEqual(Constants.Rydberg_inf(),Constants.rydberg_inf_constant())


class ConstantsRydbergH(unittest.TestCase):
    def test_rydberg_h(self):
        Rydberg_inf = Constants.Rydberg_inf()
        m_p = Constants.m_p()
        m_e = Constants.m_e()
        rydberg_h = Rydberg_inf * (m_p/(m_e + m_p))
        self.assertEqual(Constants.Rydberg_h(),rydberg_h)

    def test_rydberg_h_constant(self):
        self.assertEqual(Constants.Rydberg_h(),Constants.rydberg_h_constant())

