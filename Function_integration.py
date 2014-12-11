from Equation_manipulation import *
from sympy import integrate, symbols
from Simple_result_window import resultWindow
import logging

x = symbols('x')

def integrateFunctionArgsHandler(raw_args):
    args = ''.join(raw_args).strip()
    if args.startswith('integr'):
        return True
    return False

def integrateFunction(expression):
    expression = "".join(expression).split()
    assert expression[0].startswith('integr')
    expression = ''.join(expression[1:])

    d_index = expression.index("d")
    integral = getMissingMultiplic((expression[:d_index]).strip())
    variable = expression[d_index+1]
    integral = integral.replace(variable, 'x')
    # separating the integration part from the lanes part
    after_integral = (expression[d_index+2:]).strip()
    logging.info(integral)
    logging.info(after_integral)
    if after_integral == "":
        result = str(integrate(integral, x))
        # if the integral in infinite
    else:
        if "," in after_integral:
            # if lanes are separated with commas
            a = after_integral.split(",")[0].strip().strip("(")
            b = after_integral.split(",")[1].strip().strip(")")
        elif "from" in after_integral:
            m_index = after_integral.index("m")
            t_index = after_integral.index("t")
            a = after_integral[m_index+1:t_index].strip()
            b = after_integral[t_index+2:].strip()
        elif "ni" in after_integral:
            t_index = after_integral.index("t")
            if after_integral[t_index-2] == "-":
                a = after_integral[:t_index-2]
            else:
                a = after_integral[:t_index-1]
            n_index = after_integral.index("n")
            if after_integral[n_index-1] == "-":
                b = after_integral[t_index+1:n_index-1].strip()
            else:
                b = after_integral[t_index+1:n_index].strip()
        result = str(integrate(integral, (x, float(a), float(b))))
    result = result.replace("x", variable)
    expression = "integraal (" + expression + ")"
    try:
        result = round(float(result), 2)
    except ValueError:
        pass
    resultWindow(result, expression)
    logging.info(result)

if __name__ == '__main__':
    print(integrateFunction(["2y dy from 3 to 5"]))
    # print(integrateFunction("(x**2 + 2x)dx  3st 5ni"))
    # print(integrateFunction("2x dx (2,9)"))
    # print(integrateFunction("2y dy"))
    # print(integrateFunction("(x**2 + 2x)dx  3.4st 5ni"))
