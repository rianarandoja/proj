from sympy.physics.units import *
from Simple_result_window import resultWindow
import logging

added_units = ({"pints": "liters=0.568261", "gallon": "liters=4.54609",
                "pound": "kg=0.453592", "ounce": "kg=0.0283495", "stone": "kg=6.35029",
                "grain": "kg=0.00006479891", "pint": "liters=0.568261", "gallons": "liters=4.54609",
                "ounces": "kg=0.0283495", "pounds": "kg=0.453592", "stones": "kg=6.35029",
                "grains": "kg=0.00006479891"})

f_list = ["Fahrenheit", "fahrenheit", "F"]
k_list = ["Kelvin", "kelvin", "K"]
c_list = ["Celsius", "celsius", "C"]

def convertUnits(command):
    command = "".join(command)
    if " to " in command:
        separator_index = command.index(" to ")
        to_unit = command[separator_index+3:].strip()
    elif " in " in command:
        separator_index = command.index(" in ")
        to_unit = command[separator_index+3:].strip()
    elif "->" in command:
        separator_index = command.index("->")
        to_unit = command[separator_index+2:].strip()
    else:
        return -1
    convert_from = (command[:separator_index]).strip()
    for i in range(len(convert_from)):
        if convert_from[i].isdigit() and convert_from[i+1] != "." and not convert_from[i+1].isdigit():
            convertible = float(convert_from[:i+1].strip())
            from_unit = convert_from[i+1:].strip()
            break
    logging.info(convertible)
    logging.info(from_unit)
    logging.info(to_unit)
    if from_unit in c_list or from_unit in k_list or from_unit in f_list:
        # temperature
        if from_unit in f_list:
            if to_unit in c_list:
                answer = (convertible-32) * (5/9)
            elif to_unit in k_list:
                answer = (convertible-32) * (5/9) + 273.15
        elif from_unit in k_list:
            if to_unit in c_list:
                answer = convertible - 273.15
            elif to_unit in f_list:
                answer = (convertible - 273.15) * (9/5) + 32
        elif from_unit in c_list:
            if to_unit in f_list:
                answer = convertible * (9/5) + 32
            elif to_unit in k_list:
                answer = convertible + 273.15

    elif (find_unit(from_unit) != [] and find_unit(to_unit) != [] and from_unit != ("pounds" or "pound")
          and to_unit != ("pounds" or "pound")):
            # SI units
            answer = convertible * eval(from_unit) / eval(to_unit)

    else:
        # other self-added units
        if find_unit(from_unit) != []:
            unit = added_units[to_unit].split("=")[0]
            konstant = added_units[to_unit].split("=")[1]
            number = float(convertible)/float(konstant)
            answer = number * eval(from_unit) / eval(unit)

        elif find_unit(to_unit) != []:
            unit = added_units[from_unit].split("=")[0]
            konstant = added_units[from_unit].split("=")[1]
            number = float(convertible)*float(konstant)
            answer = number * eval(unit) / eval(to_unit)

        else:
            if added_units[from_unit].split("=")[0] == added_units[to_unit].split("=")[0]:
                answer = ((float(convertible)*float(added_units[from_unit].split("=")[1])) /
                                                        float(added_units[to_unit].split("=")[1]))
            else:
                return -1
    logging.info(answer)
    try:
        result = str(round(float(answer), 2)) + " " + to_unit
    except TypeError:
        return -1
    logging.info(result)
    resultWindow(result, command)
    return result


if __name__ == '__main__':
    # print(convertUnits(["2 liters to pints"]))
    print(convertUnits("2 pints to liters"))
    # print(convertUnits("40 m in pints"))
    # print(convertUnits("2 kg in ounces"))
    # print(convertUnits("1 kg to pounds"))
    # print(convertUnits("-40C to F"))
    print(convertUnits("0 F to K"))
    # print(convertUnits("33K to C"))
