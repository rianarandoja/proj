from Equation_manipulation import *
from sympy import integrate, symbols

x = symbols('x')

def getStringsRemoved(argument):
    # removes strings from argument, so there stay only numbers and minuses
    rem = []
    for el in argument:
        if not el.isdigit() and el != "-" and el != ".":
            rem.append(el)
    for i in range(len(rem)):
        argument.remove(rem[i])
    return argument

def integrateFunction(expression):
    d_index = expression.index("d")
    integral = list(getMissingMultiplic((expression[:d_index]).strip()))
    variable = expression[d_index+1]
    integral = ''.join(integral).replace(variable, 'x')
    # separating the integration part from the lanes part
    after_integral = (expression[d_index+2:]).strip()
    if after_integral == "":
        result = str(integrate(integral, x))
        # if the integral in infinite
    else:
        if "," in after_integral:
        # if lanes are separated with commas
            a = list(after_integral.split(",")[0].strip())
            b = list(after_integral.split(",")[1].strip())
        else:
            spaces = after_integral.count(" ")
            # if lanes are written down with words, it counts spaces
            if spaces == 1:
                a = list(after_integral.split(" ")[0].strip())
                b = list(after_integral.split(" ")[1].strip())
            elif spaces == 3:
                a = list(after_integral.split(" ")[1])
                b = list(after_integral.split(" ")[3])
        a = float("".join(getStringsRemoved(a)))
        b = float("".join(getStringsRemoved(b)))
        result = str(integrate(integral, (x, a, b)))
    result = result.replace("x", variable)
    try:
        result = round(float(result), 2)
    except ValueError:
        result = result
    return result

if __name__ == '__main__':
    print(integrateFunction("2y dy from 3 to 5"))
    print(integrateFunction("(x**2 + 2x)dx  3st 5ni"))
    print(integrateFunction("2x dx (2,9)"))
    print(integrateFunction("2y dy"))
    print(integrateFunction("(x**2 + 2x)dx  3.4st 5ni"))
