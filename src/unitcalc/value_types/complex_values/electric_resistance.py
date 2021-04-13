from ..value import SIValue

class Ohm(SIValue):
    _re_pattern = "^[Oo]hm$|^Ω$"

    def __init__(self,value,prefix:str=""):
        super().__init__(value,prefix=prefix,
                         kg=1,m=2,
                         sec=-3,A=-2)

    def _base_symbol(self):
        return "Ω"