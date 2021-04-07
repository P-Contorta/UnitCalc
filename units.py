class Units(object):
    @classmethod
    def empty_units(cls):
        return Units(sec=0,m=0,kg=0,K=0,A=0,mol=0,cd=0)

    def __init__(self,sec=0,m=0,kg=0,K=0,A=0,mol=0,cd=0):
        self._sec = sec
        self._m = m
        self._kg = kg
        self._K = K
        self._A = A
        self._mol = mol
        self._cd = cd

    def as_dict(self):
        return {"sec":self._sec,"m":self._m,"kg":self._kg,
                "K":self._K,"A":self._A,"mol":self._mol,
                "cd":self._cd}

    # Overload Mult method
    def __mul__(self,other):
        if isinstance(other,Units):
            other_unit_container = other.as_dict()
            this_unit_container = self.as_dict()
            return Units(**{key: this_unit_container[key] + other_unit_container[key] for key in Units.empty_units().as_dict()})
        else:
            raise NotImplementedError("Must multiply with another Units type.")

    # Overlaod Div Method
    def __truediv__(self,other):
        if isinstance(other,Units):
            other_unit_container = other.as_dict()
            this_unit_container = self.as_dict()
            return Units(**{key: this_unit_container[key] - other_unit_container[key] for key in Units.empty_units().as_dict()})
        else:
            raise NotImplementedError("Must divide with another Units type.")


    # Overload Power Method
    def __pow__(self,modulo):
        if isinstance(modulo,(int,float)):
            this_unit_container = self.as_dict()
            return Units(**{key: this_unit_container[key]*modulo for key in Units.empty_units().as_dict()})
        else:
            raise NotImplementedError("Must take the power with an int or float.")

    # Overload == method to test for unit equality not object equality
    def __eq__(self,other):
        if isinstance(other,Units):
            other_units = other.as_dict()
            this_unit_container = self.as_dict()
            for key in Units.empty_units().as_dict():
                try:
                    self_value = this_unit_container[key] 
                    other_value = other_units[key]
                except:
                    return False
                else:
                    if other_value != self_value:
                        return False
            return True
        else:
            return False

    def __ne__(self,other):
        return not self==other

    # Print out the units
    def __repr__(self):
        numerator_value = []
        numerator_pow = []
        denominator_value = []
        denominator_pow = []
        for key, value in self.as_dict().items():
            if value > 0:
                numerator_value.append(key)
                numerator_pow.append(value)
            if value < 0:
                denominator_value.append(key)
                denominator_pow.append(value*-1)

        print_str = ""
        for i, value in enumerate(numerator_value):
            numerator_pow_val = numerator_pow[i]
            if numerator_pow_val != 1:
                print_str += "{}{} ".format(value,numerator_pow_val)
            else:
                print_str += "{} ".format(value)

        for i, value in enumerate(denominator_value):
            if i==0:
                print_str += "/ "

            denominator_val = denominator_pow[i]
            if denominator_val != 1:
                print_str += "{}{} ".format(value,denominator_val)
            else:
                print_str += "{} ".format(value)

        CODEX = str.maketrans("0123456789.","⁰¹²³⁴⁵⁶⁷⁸⁹·")
        return print_str.translate(CODEX)