from ..value import SIValue

class Candela(SIValue):
    _re_pattern = "^cd$|^[Cc]andelas?$"

    def __init__(self,value,prefix:str="",parser=None):
        super().__init__(value,
                         prefix=prefix,
                         cd=1,
                         parser=parser)

    def _base_symbol(self):
        return "cd"