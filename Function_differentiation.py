# coding=utf-8
from Equation_manipulation import isVariable, getMissingMultiplic
from sympy import symbols, diff


x = symbols('x')

def diffFunction(expr):
    for char in expr:
        if isVariable(char):
            variable = char
    expr = getMissingMultiplic(expr)
    expr = expr.replace(variable, 'x')
    result = str(diff(expr, x))
    result = result.replace('x', variable)
    return result

if __name__ == '__main__':
    print(diffFunction("x**2"))
    print(diffFunction("2q"))
    print(diffFunction("sin(x)"))
