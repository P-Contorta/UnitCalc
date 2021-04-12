from value_types.value import SIValue

import math

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


    def parse_symbols(self,units)->str:
        numerator_units = []
        demoninator_units = []

        units_to_parse_dict = units.as_dict().copy()
        for i, parse_units in enumerate(self._unit_order):
            parse_w_dict = parse_units.as_dict()

            closest_to_zero_scale = None
            for key in parse_w_dict:
                parse_w_value = parse_w_dict[key]
                if parse_w_value == 0:
                    continue
                else:
                    value_to_parse = units_to_parse_dict[key]

                raw_scale = value_to_parse/parse_w_value
                if raw_scale > 0:
                    scale = math.floor(raw_scale)
                else:
                    scale = math.ceil(raw_scale)

                if closest_to_zero_scale is None:
                    closest_to_zero_scale = scale
                elif scale < 0:
                    closest_to_zero_scale = max(closest_to_zero_scale,scale)
                elif scale > 0:
                    closest_to_zero_scale = min(closest_to_zero_scale,scale)
                else:
                    closest_to_zero_scale = 0

            if closest_to_zero_scale != 0:
                if closest_to_zero_scale > 0:
                    if closest_to_zero_scale == 1:
                        numerator_units.append(str(self._symbol_order[i]))
                    else:
                        numerator_units.append("{}{}".format(self._symbol_order[i],
                                                            closest_to_zero_scale))
                else:
                    if closest_to_zero_scale == -1:
                        demoninator_units.append(str(self._symbol_order[i]))
                    else:
                        demoninator_units.append("{}{}".format(self._symbol_order[i],
                                                            closest_to_zero_scale*-1))

                for key in parse_w_dict:
                    parse_w_value = parse_w_dict[key]
                    units_to_parse_dict[key] = units_to_parse_dict[key] - parse_w_value*closest_to_zero_scale


        for key in units_to_parse_dict:
            value = units_to_parse_dict[key]
            if value > 0:
                if value == 1:
                    numerator_units.append(str(key))
                else:
                    numerator_units.append("{}{}".format(key,value))
            elif value < 0:
                if value == -1:
                    demoninator_units.append(str(key))
                else:
                    demoninator_units.append("{}{}".format(key,value*-1))
            else:
                continue
      
        numerator_str = " ".join(numerator_units)
        denominator_str = " ".join(demoninator_units)
        if denominator_str != "":
            print_str = "{} / {}".format(numerator_str,denominator_str)
        else:
            print_str = numerator_str

        CODEX = str.maketrans("0123456789.","⁰¹²³⁴⁵⁶⁷⁸⁹·")
        return print_str.translate(CODEX)


    def __repr__(self):
        print_str = "{} parse order:\n".format(self.__class__.__name__)
        for i,symbol in enumerate(self._symbol_order):
            if i == 0:
                print_str += " - {}".format(symbol)
            else:
                print_str += "\n - {}".format(symbol)
        return print_str