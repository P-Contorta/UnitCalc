from ..value import SIValue

class Volt(SIValue):
    _re_pattern = "^V$|^[Vv]olts?$"

    def __init__(self,value,prefix:str="",parser=None):
        super().__init__(value,
                         prefix=prefix,
                         kg=1,m=2,
                         sec=-3,A=-1,
                         parser=parser)

    def _base_symbol(self):
        return "V"