from ..value import SIValue

class Watt(SIValue):
    _re_pattern = "^W$|^[Ww]atts?$"

    def __init__(self,value,prefix:str="",parser=None):
        super().__init__(value,
                         prefix=prefix,
                         kg=1,m=2,
                         sec=-3,
                         parser=parser)

    def _base_symbol(self):
        return "W"