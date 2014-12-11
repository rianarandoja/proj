# coding=utf-8
from Equation_manipulation import isVariable, getMissingMultiplic
from sympy import symbols, diff
from Simple_result_window import resultWindow
import logging

x = symbols('x')

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
    result = solveDiff(user_input)
    logging.info(result)
    resultWindow(result, user_input)

if __name__ == '__main__':
    print(diffFunction(["sin(x)"]))
