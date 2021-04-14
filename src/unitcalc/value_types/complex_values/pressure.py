from ..value import SIValue

class Pascal(SIValue):
    _re_pattern = "^Pa$|^[Pp]ascals?$"

    def __init__(self,value,prefix:str="",parser=None):
        super().__init__(value,
                         prefix=prefix,
                         kg=1,
                         m=-1,sec=-2,
                         parser=parser)
  
    def _base_symbol(self):
        return "Pa"