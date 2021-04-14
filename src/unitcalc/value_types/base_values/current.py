from ..value import SIValue

class Ampere(SIValue):
    _re_pattern = "^A$|^[Aa]mp(ere)?s?$"

    def __init__(self,value,prefix:str="",parser=None):
        super().__init__(value,
                         prefix=prefix,
                         A=1,
                         parser=parser)

    def _base_symbol(self):
        return "A"