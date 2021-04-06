from value_types.value import SIValue

class Ampere(SIValue):
    _re_pattern = "A$|[Aa]mp(ere)?s?$"

    def __init__(self,value,prefix:str=""):
        super().__init__(value,prefix=prefix,A=1)

    def _base_symbol(self):
        return "A"