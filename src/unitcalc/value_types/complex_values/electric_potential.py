from ..value import SIValue

class Volt(SIValue):
    _re_pattern = "^V$|^[Vv]olts?$"

    def __init__(self,value,prefix:str=""):
        super().__init__(value,prefix=prefix,
                         kg=1,m=2,
                         sec=-3,A=-1)

    def _base_symbol(self):
        return "V"