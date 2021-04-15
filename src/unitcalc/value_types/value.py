from ..units import Units
import re

class CustomValue(object):
    @classmethod
    def is_value(cls,value_name:str):
        return False

    def __init__(self,value,sec=0,m=0,kg=0,K=0,A=0,mol=0,cd=0):
        if not isinstance(value,(int,float)):
            raise AttributeError("CustomValue only takes int or float values as input.")

        # Parameters
        self._value = value
        self._si_units = Units(sec=sec,m=m,kg=kg,K=K,A=A,mol=mol,cd=cd)
        self._symbol = str(self._si_units)

    def value(self):
        return self._value

    def si_value(self):
        return self.value()

    def central_value(self):
        return self.si_value()

    def symbol(self):
        return self._symbol
        
    def si_symbol(self):
        return self.symbol()

    def si_units(self):
        return self._si_units


    def __repr__(self):
        si_symbol_str = self.si_symbol()
        if si_symbol_str == "":
            return "{}".format(self.si_value())
        else:
            return "{} {}".format(self.si_value(),si_symbol_str)


    # Math
    def __add__(self,other):
        if isinstance(other,(CustomValue,SIValue,NonSIValue)):
            if self.si_units() == other.si_units():
                return CustomValue(self.central_value() + other.central_value(), **self.si_units().as_dict())
            else:
                raise ValueError("Cannot perform addition because the units do not match.")

        elif isinstance(other,(float,int)):
            if self.si_units() == Units():
                return CustomValue(self.value() + other, **self.si_units().as_dict())
            raise ValueError("Cannot add a dimensionless unit to a dimensioned unit.")
        else:
            raise AttributeError("Can only add objects with type int, float, CustomValue, SIValue, or NonSIValue.")

    def __radd__(self,other):
        return self + other

    def __sub__(self,other):
        if isinstance(other,(CustomValue,SIValue,NonSIValue)):
            if self.si_units() == other.si_units():
                return CustomValue(self.central_value() - other.central_value(), **self.si_units().as_dict())
            else:
                raise ValueError("Cannot perform subtraction because the units do not match.")

        elif isinstance(other,(float,int)):
            if self.si_units() == Units():
                return CustomValue(self.value() - other, **self.si_units().as_dict())
            raise ValueError("Cannot subtract a dimensionless unit from a dimensioned unit.")
        else:
            raise AttributeError("Can only subtract objects with type int, float, CustomValue, SIValue, or NonSIValue.")

    def __rsub__(self,other):
        return (self - other) * -1

    def __mul__(self,other):
        if isinstance(other,(CustomValue,SIValue,NonSIValue)):
            return CustomValue(self.central_value() * other.central_value(), **(self.si_units()*other.si_units()).as_dict())
        elif isinstance(other,(float,int)):
            return CustomValue(self.value() * other, **self.si_units().as_dict())
        else:
            raise AttributeError("Can only multiply objects with type int, float, CustomValue, SIValue, or NonSIValue.")

    def __rmul__(self,other):
        return self*other

    def __truediv__(self,other):
        if isinstance(other,(CustomValue,SIValue,NonSIValue)):
            return CustomValue(self.central_value() / other.central_value(), **(self.si_units()/other.si_units()).as_dict())
        elif isinstance(other,(float,int)):
            return CustomValue(self.value() / other, **self.si_units().as_dict())
        else:
            raise AttributeError("Can only divide objects with type int, float, CustomValue, SIValue, or NonSIValue.")

    def __rtruediv__(self,other):
        return (self / other)**-1

    def __pow__(self,modulo):
        if isinstance(modulo,(int,float)):
            return CustomValue(self.central_value()**modulo, **(self.si_units()**modulo).as_dict())
        else:
            raise AttributeError("Can only take a power with an object that has a type int or float.")


    # Bool
    def __eq__(self,other):
        if isinstance(other,(CustomValue,SIValue,NonSIValue)):
            if self.si_units() == other.si_units():
                if self.central_value() == other.central_value():
                    return True
            return False
        else:
            if self.si_units() == Units():
                if self.value() == other:
                    return True
            return False

    def __ne__(self,other):
        return not self == other

    def __lt__(self,other):
        if isinstance(other,(CustomValue,SIValue,NonSIValue)):
            if self.si_units() == other.si_units():
                if self.central_value() < other.central_value():
                    return True
            return False
        else:
            if self.si_units() == Units():
                if self.value() < other:
                    return True
            return False

    def __ge__(self,other):
        return not self < other

    def __gt__(self,other):
        if isinstance(other,(CustomValue,SIValue,NonSIValue)):
            if self.si_units() == other.si_units():
                if self.central_value() > other.central_value():
                    return True
            return False
        else:
            if self.si_units() == Units():
                if self.value() > other:
                    return True
            return False

    def __le__(self,other):
        return not self > other




class SIValue(object):
    _re_pattern = None

    @classmethod
    def is_value(cls,value_str:str)->bool:
        if cls._re_pattern is None:
            raise NotImplementedError("{} must overload cls._re_pattern with a non-None value."\
                                      .format(self.__class__.__name__))
        if not isinstance(cls._re_pattern,str):
            raise AttributeError("{} has a non-string value for cls._re_pattern. cls._re_pattern must be a str."\
                                 .format(self.__class__.__name__))
        return bool(re.search(cls._re_pattern,value_str))

    def __init__(self,value,prefix="",center_prefix="",
                      sec=0,m=0,kg=0,K=0,A=0,mol=0,cd=0):
        if not isinstance(value,(int,float,complex)):
            raise AttributeError("SIValue only takes int, float, or complex values as input.")

        # Parameters
        self._prefix, self._power = self._parse_prefix(prefix)
        self._center_prefix, self._center_power = self._parse_prefix(center_prefix)

        self._value = value
        self._central_value = self.value() * 10**(self._power-self._center_power)

        self._si_units = Units(sec=sec,m=m,kg=kg,K=K,A=A,mol=mol,cd=cd)
        self._symbol = self._prefix + self._base_symbol()


    def _base_symbol(self):
        raise NotImplementedError("{} needs to have _base_symbol overloaded.".format(self.__class__.__name__))
        return "<base-symbol-str>"


    def _parse_prefix(self,name:str)-> (str,int):
        yocto_re = "^y(octo)?$|^Yocto$"
        zepto_re = "^z(epto)?$|^Zepto$"
        atto_re = "^a(tto)?$|^Atto$"
        femto_re = "^f(emto)?$|^Femto$"
        pico_re = "^p(ico)?$|^Pico$"
        nano_re = "^n(ano)?$|^Nano$"
        micro_re= "^μ$|^[Mm]icro$"
        mili_re = "^m(ili)?$|^[M]ili$"
        centi_re = "^c(enti)?$|^Centi$"
        deci_re = "^d(eci)?$|^Deci$"

        deca_re = "^da$|^[Dd]eca$"
        hecto_re = "^h(ecto)?$|^Hecto$"
        kilo_re = "^k(ilo)?$|^Kilo+$"
        mega_re = "^M$|^[Mm]ega$"
        giga_re = "^G$|^[Gg]iga$"
        tera_re = "^T$|^[Tt]era$"
        peta_re = "^P$|^[Pp]eta$"
        exa_re = "^E$|^[Ee]xa$"
        zetta_re = "Z$|^[Zz]etta$"
        yotta_re = "^Y$|^[Yy]otta$"
        # Value Prefix parsing
        if name is None or name == "":
            return "", 0

        if re.search(yocto_re,name):
            return "y", -24
        elif re.search(zepto_re,name):
            return "z", -21
        elif re.search(atto_re,name):
            return "a", -18
        elif re.search(femto_re,name):
            return "f", -15
        elif re.search(pico_re,name):
            return "p", -12
        elif re.search(nano_re,name):
            return "n", -9
        elif re.search(micro_re,name):
            return "μ", -6
        elif re.search(mili_re,name):
            return "m", -3
        elif re.search(centi_re,name):
            return "c", -2
        elif re.search(deci_re,name):
            return "d", -1
        elif re.search(deca_re,name):
            return "da", 1
        elif re.search(hecto_re,name):
            return "h", 2
        elif re.search(kilo_re,name):
            return "k", 3
        elif re.search(mega_re,name):
            return "M", 6
        elif re.search(giga_re,name):
            return "G", 9
        elif re.search(tera_re,name):
            return "T", 12
        elif re.search(peta_re,name):
            return "P", 15
        elif re.search(exa_re,name):
            return "E", 18
        elif re.search(zetta_re,name):
            return "Z", 21
        elif re.search(yotta_re,name):
            return "Y", 24
        else:
            raise AttributeError("{} is not a valid name.".format(name))

    def value(self):
        return self._value

    def si_value(self):
        return self.value()

    def central_value(self):
        return self._central_value


    def symbol(self):
        return self._symbol

    def si_symbol(self):
        return self.symbol()

    def central_symbol(self):
        return self._center_prefix + self._base_symbol()

    def si_units(self):
        return self._si_units

    def convert_to_unit(self,unit_name):
        if self.__class__.is_value(unit_name):
            return self
        else:
            raise ValueError("Cannot convert to {}.".format(unit_name))

    def convert_to_prefix(self,new_prefix:str):
        new_symbol, new_pow = self._parse_prefix(new_prefix)
        new_val = self._central_value * 10**(self._center_power-new_pow)
        return self.__class__(new_val,prefix=new_prefix)


    def __repr__(self):
        return "{} {}".format(self.si_value(),self.si_symbol())

    # Math
    def __add__(self,other):
        if isinstance(other,(CustomValue,SIValue,NonSIValue)):
            if self.si_units() == other.si_units():
                return self.__class__(self.central_value() + other.central_value()).convert_to_prefix(self._prefix)
            else:
                raise ValueError("Cannot perform addition because the units do not match.")
        else:
            raise AttributeError("Can only add objects with type CustomValue, SIValue, or NonSIValue.")

    def __radd__(self,other):
        return self + other

    def __sub__(self,other):
        if isinstance(other,(CustomValue,SIValue,NonSIValue)):
            if self.si_units() == other.si_units():
                
                return self.__class__(self.central_value() - other.central_value()).convert_to_prefix(self._prefix)
            else:
                raise ValueError("Cannot perform subtraction because the units do not match.")
        else:
            raise AttributeError("Can only subtract objects with type CustomValue, SIValue, or NonSIValue.")

    def __rsub__(self,other):
        return (self - other) * -1

    def __mul__(self,other):
        if isinstance(other,(CustomValue,SIValue,NonSIValue)):
            return CustomValue(self.central_value() * other.central_value(), **(self.si_units()*other.si_units()).as_dict())
        elif isinstance(other,(float,int,complex)):
            return self.__class__(self.value() * other, prefix=self._prefix)
        else:
            raise AttributeError("Can only multiply objects with type int, float, complex, SIValue, NonSIValue, or CustomValue.")

    def __rmul__(self,other):
        return self*other

    def __truediv__(self,other):
        if isinstance(other,(CustomValue,SIValue,NonSIValue)):
            return CustomValue(self.central_value() / other.central_value(), **(self.si_units()/other.si_units()).as_dict())
        elif isinstance(other,(float,int,complex)):
            return self.__class__(self.value() / other, prefix=self._prefix)
        else:
            raise AttributeError("Can only divide objects with type int, float, complex, SIValue, NonSIValue or CustomValue.")

    def __rtruediv__(self,other):
        return (self / other)**-1

    def __pow__(self,modulo):
        if isinstance(modulo,(int,float,complex)):
            return CustomValue(self.central_value()**modulo, **(self.si_units()**modulo).as_dict())
        else:
            raise AttributeError("Can only take a power with an object that has a type int, float, or complex.")


    # Bool
    def __eq__(self,other):
        if isinstance(other,(CustomValue,SIValue,NonSIValue)):
            if self.si_units() == other.si_units():
                if self.central_value() == other.central_value():
                    return True
            return False
        else:
            if self.si_units() == Units():
                if self.value() == other:
                    return True
            return False

    def __ne__(self,other):
        return not self == other

    def __lt__(self,other):
        if isinstance(other,(CustomValue,SIValue,NonSIValue)):
            if self.si_units() == other.si_units():
                if self.central_value() < other.central_value():
                    return True
            return False
        else:
            if self.si_units() == Units():
                if self.value() < other:
                    return True
            return False

    def __ge__(self,other):
        return not self < other

    def __gt__(self,other):
        if isinstance(other,(CustomValue,SIValue,NonSIValue)):
            if self.si_units() == other.si_units():
                if self.central_value() > other.central_value():
                    return True
            return False
        else:
            if self.si_units() == Units():
                if self.value() > other:
                    return True
            return False

    def __le__(self,other):
        return not self > other

class NonSIValue(object):
    _re_pattern = None

    @classmethod
    def is_value(cls,value_str:str)->bool:
        if cls._re_pattern is None:
            raise NotImplementedError("{} must overload cls._re_pattern. with a non-None value."\
                                      .format(self.__class__.__name__))
        if not isinstance(cls._re_pattern,str):
            raise AttributeError("{} has a non-string value for cls._re_pattern. cls._re_pattern must be a str."\
                                 .format(self.__class__.__name__))
        return bool(re.search(cls._re_pattern,value_str))


    def __init__(self,value,si_parent,sec=0,m=0,kg=0,K=0,A=0,mol=0,cd=0):
        if not isinstance(value,(int,float,complex)):
            raise AttributeError("NonSIValue only takes int, float, or complex values as input.")

        # Parameters
        self._value = value
        self._si_parent = si_parent

        self._si_units = Units(sec=sec,m=m,kg=kg,K=K,A=A,mol=mol,cd=cd)
        self._symbol = self._base_symbol()

    def _base_symbol(self):
        raise NotImplementedError("{} needs to have _base_symbol overloaded.".format(self.__class__.__name__))
        return "<base-symbol-str>"


    def value(self):
        return self._value

    def si_value(self):
        return self._si_parent.value()

    def central_value(self):
        return self._si_parent.central_value()

    def symbol(self):
        return self._symbol
        
    def si_symbol(self):
        return self._si_parent.symbol()

    def si_units(self):
        return self._si_units

    def convert_to_unit(self,unit_name:str):
        return self._si_parent.convert_to_unit(unit_name)



    def __repr__(self):
        return "{} {}".format(self.value(),self.symbol())

    # Math
    def __add__(self,other):
        if isinstance(other,(CustomValue,SIValue,NonSIValue)):
            if self.si_units() == other.si_units():
                return self._si_parent.__class__(self.central_value() + other.central_value()).convert_to_unit(self._symbol)
            else:
                raise ValueError("Cannot perform addition because the units do not match.")
        else:
            raise AttributeError("Can only add objects with type CustomValue, SIValue, or NonSIValue.")

    def __radd__(self,other):
        return self + other

    def __sub__(self,other):
        if isinstance(other,(CustomValue,SIValue,NonSIValue)):
            if self.si_units() == other.si_units():
                return self._si_parent.__class__(self.central_value() - other.central_value()).convert_to_unit(self._symbol)
            else:
                raise ValueError("Cannot perform subtraction because the units do not match.")
        else:
            raise AttributeError("Can only subtract objects with type CustomValue, SIValue, or NonSIValue.")

    def __rsub__(self,other):
        return (self - other) * -1

    def __mul__(self,other):
        if isinstance(other,(CustomValue,SIValue,NonSIValue)):
            return CustomValue(self.central_value() * other.central_value(), **(self.si_units()*other.si_units()).as_dict())
        elif isinstance(other,(float,int,complex)):
            return self._si_parent.__class__(self.central_value() * other).convert_to_unit(self._symbol)
        else:
            raise AttributeError("Can only multiply objects with type int, float, complex, SIValue, NonSIValue, or CustomValue.")

    def __rmul__(self,other):
        return self*other

    def __truediv__(self,other):
        if isinstance(other,(CustomValue,SIValue,NonSIValue)):
            return CustomValue(self.central_value() / other.central_value(), **(self.si_units()/other.si_units()).as_dict())
        elif isinstance(other,(float,int,complex)):
            return self._si_parent.__class__(self.central_value() / other).convert_to_unit(self._symbol)
        else:
            raise AttributeError("Can only divide objects with type int, float, complex, SIValue, NonSIValue, or CustomValue.")

    def __rtruediv__(self,other):
        return (self / other)**-1

    def __pow__(self,modulo):
        if isinstance(modulo,(int,float,complex)):
            return CustomValue(self.central_value()**modulo, **(self.si_units()**modulo).as_dict())
        else:
            raise AttributeError("Can only take a power with an object that has a type int, float, or complex.")


    # Bool
    def __eq__(self,other):
        if isinstance(other,(CustomValue,SIValue,NonSIValue)):
            if self.si_units() == other.si_units():
                if self.central_value() == other.central_value():
                    return True
            return False
        else:
            if self.si_units() == Units():
                if self.value() == other:
                    return True
            return False

    def __ne__(self,other):
        return not self == other

    def __lt__(self,other):
        if isinstance(other,(CustomValue,SIValue,NonSIValue)):
            if self.si_units() == other.si_units():
                if self.central_value() < other.central_value():
                    return True
            return False
        else:
            if self.si_units() == Units():
                if self.value() < other:
                    return True
            return False

    def __ge__(self,other):
        return not self < other

    def __gt__(self,other):
        if isinstance(other,(CustomValue,SIValue,NonSIValue)):
            if self.si_units() == other.si_units():
                if self.central_value() > other.central_value():
                    return True
            return False
        else:
            if self.si_units() == Units():
                if self.value() > other:
                    return True
            return False

    def __le__(self,other):
        return not self > other