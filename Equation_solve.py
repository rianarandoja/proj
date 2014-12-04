# coding=utf-8
from Equation_manipulation import isVariable
from Equation_manipulation import optimizeEquationForSympy
from sympy import symbols, solve


x = symbols("x")

def solveEquationArgsHandler(args):
    if '=' in ''.join(args):
        return True
    return False

def solveEquation(equation):
    equation = ''.join(equation)
    if "sqrt" in equation:
        counter = 0
        sqrt_counter = equation.count("sqrt")
        while sqrt_counter > counter:
            first_paren = equation.index("sqrt")
            after_paren = equation[first_paren+4:]
            counter_parens = 0
            for i in range(len(after_paren)):
                if after_paren[i] == "(":
                    counter_parens += 1
                elif after_paren[i] == ")":
                    counter_parens -= 1
                    if counter_parens == 0:
                        paren_index = i
                        break
            equation = ("".join(equation[:first_paren]) +
                        "".join(after_paren[:paren_index+1]) +
                        "**0.5" +
                        "".join(after_paren[paren_index+1:]))
            counter += 1
    for char in equation:
        if isVariable(char):
            variable = char
    equation = optimizeEquationForSympy(equation)
    equation = equation.replace(variable, "x")
    results = solve(equation, "x")
    for i in range(len(results)):
        try:
            results[i] = round(float(results[i]), 3)
        except ValueError:
            continue
    output = ""
    for i, result in enumerate(results):
        output += "x_%i = %s\n" %(i+1, str(result))

    output = (output.replace("x", variable)
                    .replace("I", "i"))
    return output

if __name__ == '__main__':
    print(solveEquation("1 = sin(x)"))
