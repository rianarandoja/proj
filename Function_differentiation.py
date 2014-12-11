# coding=utf-8
from Equation_manipulation import isVariable, getMissingMultiplic
from sympy import symbols, diff
from Simple_result_window import resultWindow
import logging

x = symbols('x')

def solveDiffArgsHandler(raw_args):
    args = ''.join(raw_args).strip()
    if args.startswith('dif') or args.endswith("'"):
        return True
    return False

def solveDiff(expr):
    expr = "".join(expr)
    for char in expr:
        if isVariable(char):
            variable = char
    expr = getMissingMultiplic(expr)
    expr = expr.replace(variable, 'x')
    result = str(diff(expr, x))
    result = result.replace('x', variable)
    return result

def diffFunction(user_input):
    user_input = "".join(user_input)
    if user_input.split()[0] in {'dif','diff'}:
        user_input = ''.join(user_input.split()[1:])
    if user_input.endswith("'"):
        user_input = user_input[:-1]

    user_input = user_input.replace('=','').replace('y','').replace('f(x)','')

    result = solveDiff(user_input)
    logging.info(result)
    user_input = "(%s)'" %user_input
    resultWindow(result, user_input)

if __name__ == '__main__':
    print(diffFunction(["sin(x)"]))
