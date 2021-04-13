from ..value import SIValue

class Joule(SIValue):
    _re_pattern = "^J$|^[Jj]oules?$"

    def __init__(self,value,prefix:str=""):
        super().__init__(value,prefix=prefix,
                         kg=1,m=2,
                         sec=-2)

    def _base_symbol(self):
        return "J"