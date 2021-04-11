from value_types.value import SIValue

class SIUnitParser(object):
    def __init__(self,*values:SIValue):
        self._unit_order = []
        self._symbol_order = []
        for value in values:
            if not issubclass(value,SIValue):
                raise AttributeError("SIUnitParser only accepts SIValue objects as arguments")
            else:
                _ = value(0)
                self._unit_order.append(_.si_units())
                self._symbol_order.append(_.si_symbol())

    def parse(self,units)->str:
        for i, parse_units in enumerate(self._unit_order):

            self.diff_units(parse_units,units)

        return ""


    def diff_units(self,unit_1,unit_2):
        unit_1_dict = unit_1.as_dict()
        unit_2_dict = unit_2.as_dict()
        for key in unit_1_dict:
            value_1 = unit_1_dict[key]
            if value_1 == 0:
                continue
            else:
                value_2 = unit_2_dict[key]

            value_modulo = value_2 % value_1
            print()

            if value_2 > 0:
                value_2_is_pos = True
            elif value_2 < 0:
                value_2_is_pos = False
            else:
                value_2_is_pos = None

            # negative case

            # postive case