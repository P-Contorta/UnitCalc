from ..value import SIValue

class Pascal(SIValue):
    _re_pattern = "^Pa$|^[Pp]ascals?$"

    def __init__(self,value,prefix:str=""):
        super().__init__(value,prefix=prefix,
                         kg=1,
                         m=-1,sec=-2)
  
    def _base_symbol(self):
        return "Pa"