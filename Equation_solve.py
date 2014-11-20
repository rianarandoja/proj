# coding=utf-8
from Equation_manipulation import isVariable
from Equation_manipulation import optimizeEquationForSympy
from sympy import symbols, solve


x = symbols("x")

def solveEquation(equation):
    variable = ""
    for char in equation:
        if isVariable(char):
            variable = char
    equation = optimizeEquationForSympy(equation)
    equation = equation.replace(variable, "x")
    result = solve(equation, "x")
    output = ""
    for i in range(len(result)):
        output += "x_" + str(i+1) + " = " + str(result[i]) + "\n"
    output = (output.replace("x", variable)
                    .replace("I", "i"))
    return output

if __name__ == '__main__':
    print(solveEquation("a = a**0.5"))
