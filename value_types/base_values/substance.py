from value_types.value import SIValue

class Mol(SIValue):
    _re_pattern = "^[Mm]ols?$"
    
    def __init__(self,value,prefix:str=""):
        super().__init__(value,prefix=prefix,mol=1)

    def _base_symbol(self):
        return "mol"