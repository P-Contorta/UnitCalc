from ..value import SIValue

class Mol(SIValue):
    _re_pattern = "^[Mm]ols?$"
    
    def __init__(self,value,prefix:str="",parser=None):
        super().__init__(value,
                         prefix=prefix,
                         mol=1,
                         parser=parser)

    def _base_symbol(self):
        return "mol"