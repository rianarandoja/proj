# coding=utf-8
from Equation_manipulation import isVariable
from sympy import symbols, diff


x = symbols('x')

def getVarInDerivative(expression):
    expression = list(expression)
    # finds the symbol from expression, that is in list of variables and not in list of variables, that cannot be
    # used while derivation, returns the variable
    unsuitable_vars = ["a", "e", "c", "o", "s", "i", "n", "t", "l", "r", "g", "h"]
    for i in range(len(expression)):
        if isVariable(expression[i]) and expression[i] not in unsuitable_vars:
            return expression[i]

def diffFunction(expression):
    variable = getVarInDerivative(expression)
    expression = list(expression)
    for i in range(len(expression)-1):
        # inserts multiplication mark between number and letter and two brackets
        if expression[i].strip().isdigit() and isVariable(expression[i+1]):
            expression.insert(i+1, "*")
        elif expression[i] == ")" and expression[i+1] == "(":
            expression.insert(i+1, "*")
    expression = ''.join(expression).replace(variable, 'x')
    result = str(diff(expression, x))
    result = result.replace('x', variable)
    return result

if __name__ == '__main__':
    print(diffFunction("x**2"))
    print(diffFunction("2x"))
    print(diffFunction("sin(x)"))
