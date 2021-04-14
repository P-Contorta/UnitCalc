from ..value import SIValue

class Coulomb(SIValue):
    _re_pattern = "^[Cc]oul(omb)?s?$"
    
    def __init__(self,value,prefix:str="",parser=None):
        super().__init__(value,
                         prefix=prefix,
                         A=1,sec=1,
                         parser=parser)

    def _base_symbol(self):
        return "C"