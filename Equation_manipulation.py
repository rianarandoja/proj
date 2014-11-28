# coding=utf-8
# from sympy import symbols

# x = symbols('x')

def isVariable(variable):
    # returns True, if the symbol is in list of variables
    list_of_variables = {'q', 'w', 'y', 'u', 'p', 'ü', 'õ', 'd', 'f', 'j', 'k','ö', 
                         'ä', 'z', 'x', 'v', 'b', 'm', 'Q', 'W', 'Y', 'U', 'P','Ü', 
                         'Õ', 'D', 'F', 'J', 'K', 'Ö', 'Ä', 'Z', 'X', 'V', 'B', 'M'}
    if variable in list_of_variables: return True
    return False

def getRidOfSpaces(argument):
    return argument.replace(' ', '')

def getMissingMultiplic(argument):
    # if there are any missing multiplication mark in the input, it adds them
    argument = list(getRidOfSpaces(argument))
    for i in range(len(argument)-1):
        if (argument[i]).strip().isdigit():
            if isVariable(argument[i+1]):
                argument.insert(i+1, "*")
            elif argument[i+1] == "(":
                argument.insert(i+1, "*")
        elif argument[i] == ")":
            if argument[i+1] == "(":
                argument.insert(i+1, "*")
            elif (argument[i+1]).strip().isdigit():
                argument.insert(i+1, "*")
            elif isVariable(argument[i+1]):
                argument.insert(i+1, "*")
        elif isVariable(argument[i]):
            if (argument[i+1]).strip().isdigit():
                argument.insert(i+1, "*")
            elif argument[i+1] == "(":
                argument.insert(i+1, "*")
    return "".join(argument)

def getAllToLeftSide(expr):
    # takes an argument as string and returns the it with all arguments on the left side with operators changed
    expr = list(getRidOfSpaces(expr))
    if "|" in expr:
        counter = 0
        for i in range(len(expr)):
            if expr[i] == "|":
                counter += 1
                if counter % 2 == 0:
                    expr[i] = ")"
    expr = "".join(expr)
    expr = list(expr.replace("|", "abs("))
    if expr.count('(') != expr.count(')'):
        return -1
    equal_sign_index = expr.index("=")
    left_side = "".join(expr[:equal_sign_index])
    right_side = expr[equal_sign_index+1:]
    counter_parens = 0
    for i in range(len(right_side)):
        if right_side[i] == "(":
            counter_parens += 1
        elif right_side[i] == ")":
            counter_parens -= 1
        if counter_parens == 0:
            if right_side[i] == "+":
                right_side[i] = "-"
            elif right_side[i] == "-":
                right_side[i] = "+"
    right_side = "".join(right_side)
    if right_side[0] != "+" and right_side[0] != "-":
        right_side = "-" + right_side
    return left_side + right_side

def optimizeEquationForSympy(equation):
    equation = getMissingMultiplic(equation)
    equation = getAllToLeftSide(equation)
    return equation

if __name__ == '__main__':
    print(optimizeEquationForSympy('3x + 7 = 6y - p**(-4)'))
    print(optimizeEquationForSympy("4-7=abs(3-2)+abs(4-7)-2(+3(4-z))"))
    print(optimizeEquationForSympy("x-7+|x-2+2|=+|4-7| + |x+6|"))
