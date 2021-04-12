from value_types.value import SIValue

class Candela(SIValue):
    _re_pattern = "^cd$|^[Cc]andelas?$"

    def __init__(self,value,prefix:str=""):
        super().__init__(value,prefix=prefix,cd=1)

    def _base_symbol(self):
        return "cd"