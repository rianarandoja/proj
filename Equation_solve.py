# coding=utf-8
from Equation_manipulation import isVariable
from Equation_manipulation import optimizeEquationForSympy
from sympy import symbols, solve


x = symbols("x")

def solveEquation(equation):
    if "sqrt" in equation:
        equation = equation.split("sqrt(")
        index = equation[1].index(")")
        equation[1] = equation[1][:index] + "**0.5" + equation[1][index+1:]
        equation = "".join(equation[0]+equation[1])
    variable = ""
    for char in equation:
        if isVariable(char):
            variable = char
    equation = optimizeEquationForSympy(equation)
    equation = equation.replace(variable, "x")
    result = solve(equation, "x")
    for i in range(len(result)):
        try:
            result[i] = round(float(result[i]), 3)
        except ValueError:
            result[i] = result[i]
    output = ""
    for i in range(len(result)):
        output += "x_" + str(i+1) + " = " + str(result[i]) + "\n"
    output = (output.replace("x", variable)
                    .replace("I", "i"))
    return output

if __name__ == '__main__':
    print(solveEquation("a = a**0.5"))
