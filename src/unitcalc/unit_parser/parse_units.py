from ..value_types.value import SIValue

import math

class SIUnitParser(object):
    def __init__(self,*values:SIValue):
        self._value_order = []
        for value in values:
            if not issubclass(value,SIValue):
                raise AttributeError("SIUnitParser only accepts SIValue objects as arguments")
            else:
                # Init method to get access to units
                # classmethod doesn't work with current value object design
                self._value_order.append(value(0))


    # Simplify by trying to remove the most base SI units per pass -- Greedy Algo
    # all objects passed in are modified
    def _recurrent_symbol_parse(self,parse_units,units_to_parse:dict)->(list,dict):
        units_to_parse_cp = units_to_parse.copy()
        max_tmp_value = None
        max_scale = None
        max_idx = None
        result = []
        omit_units_idx = set()
        units_result = units_to_parse
        for i,parse_unit in enumerate(parse_units):
            parse_w_si_units = parse_unit.si_units().as_dict()

            closest_to_zero_scale = None
            total_units = 0
            for key in parse_w_si_units:
                parse_w_value = parse_w_si_units[key]
                if parse_w_value == 0:
                    continue
                else:
                    value_to_parse = units_to_parse_cp[key]

                total_units += abs(parse_w_value)
                raw_scale_from_zero = value_to_parse/parse_w_value
                if raw_scale_from_zero > 0:
                    scale = math.floor(raw_scale_from_zero)
                else:
                    scale = math.ceil(raw_scale_from_zero)

                if closest_to_zero_scale is None:
                    closest_to_zero_scale = scale
                elif scale < 0:
                    closest_to_zero_scale = max(closest_to_zero_scale,scale)
                elif scale > 0:
                    closest_to_zero_scale = min(closest_to_zero_scale,scale)
                else:
                    closest_to_zero_scale = 0

            if closest_to_zero_scale is None:
                closest_to_zero_scale = 0

            
            if closest_to_zero_scale == 0:
                omit_units_idx.add(i)
                

            possible_units_simplified = abs(total_units * closest_to_zero_scale)
            if max_scale is None:
                max_scale = closest_to_zero_scale
                max_tmp_value = possible_units_simplified
                max_idx = i
                
            else:
                if possible_units_simplified > max_tmp_value:
                    max_scale = closest_to_zero_scale
                    max_tmp_value = possible_units_simplified
                    max_idx = i

        if max_scale != 0 and max_scale is not None:
            extract = parse_units.pop(max_idx)
            extract_units_dict = extract.si_units().as_dict()
            for key in extract_units_dict:
                extract_value = extract_units_dict[key]
                units_to_parse_cp[key] = units_to_parse_cp[key] - (extract_value * max_scale)
            
            result.append((extract.si_symbol(),max_scale))

            new_parse_units = []
            for i,parse_unit in enumerate(parse_units):
                if i not in omit_units_idx:
                    new_parse_units.append(parse_unit)
            recurrent_results, units_result = self._recurrent_symbol_parse(new_parse_units,units_to_parse_cp)
            result.extend(recurrent_results)

        return result, units_result




    def parse_symbols(self,units)->str:
        symbols_data, remaining_units = self._recurrent_symbol_parse(self._value_order.copy(),
                                                                     units.as_dict().copy())
        symbols_data = sorted(symbols_data,key=lambda x:abs(x[1]))

        numerator_units = []
        demoninator_units = []
 
        for symbol, power  in symbols_data:
            if power > 0:
                if power == 1:
                    numerator_units.append(symbol)
                else:
                    numerator_units.append("{}{}".format(symbol,power))
            elif power < 0:
                if power == -1:
                    demoninator_units.append(symbol)
                else:
                    demoninator_units.append("{}{}".format(symbol,power*-1))
            else:
                continue

        for symbol, power in sorted(remaining_units.items(),key=lambda x:abs(x[1])):
            if power > 0:
                if power == 1:
                    numerator_units.append(symbol)
                else:
                    numerator_units.append("{}{}".format(symbol,power))
            elif power < 0:
                if power == -1:
                    demoninator_units.append(symbol)
                else:
                    demoninator_units.append("{}{}".format(symbol,power*-1))
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