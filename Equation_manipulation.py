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

def getSignsReversed(argument):
    # changes - to + and + to -
    for i in range(len(argument)):
        if argument[i] == "-":
             argument[i] = "+"
        elif argument[i] == "+":
             argument[i] = "-"
    return argument

def getAbsToLeft(argument):
    # changes operators in the argument if there are abs in the argument
    argument = list(argument)
    between_abs = []
    for i in range(len(argument)):
        if argument[i] == "|":
            between_abs.append(i)
    abs = argument[between_abs[0]:between_abs[1]+1]
    return ("".join(getSignsReversed(argument[:between_abs[0]])) +
            "".join(abs) +
            "".join(getSignsReversed(argument[between_abs[1]+1:])))

def getParensToLeft(argument):
    # changes operators in the argument if there are parens
    first = []
    second = []
    counter = 0
    for i in range(len(argument)):
            if argument[i] == "(":
                if counter == 0:
                    first.append(i)
                counter += 1
            elif argument[i] == ")":
                counter -= 1
                if counter == 0:
                    second.append(i)
    between_parens = []
    for i in range(len(first)):
        between_parens.append(argument[first[i]:second[i]+1])
        # appends the area between parens into list
    parens = []
    # adds parens and the after parens part until the last parens
    for i in range(len(between_parens)-1):
        parens.append("".join(between_parens[i]))
        after_bracket = "".join(getSignsReversed(argument[int(second[i]+1):int(first[i+1])]))
        parens.append(after_bracket)
    parens_ = "".join(parens)
    beginning = "".join(getSignsReversed(argument[:int(first[0])]))
    last_paren = "".join(between_parens[-1])
    end = "".join(getSignsReversed(argument[int(second[-1]+1):]))
    argument = beginning + parens_ + last_paren + end
    # adds the beginning, the first parens with the area between them, last bracket and the ending
    return argument

def getAllToLeftSide(argument):
    # takes an argument as string and returns the it with all arguments on the left side with operators changed
    if argument.count('(') != argument.count(')') or argument.count('|') % 2 != 0:
        return -1

    argument = list(getRidOfSpaces(argument))
    equal_sign = argument.index("=")
    left_side = argument[:equal_sign]
    left_side = "".join(left_side)
    right_side_beginning = equal_sign+1
    right_side = argument[right_side_beginning:]
    if right_side == ["0"]:
        # checks if maybe everything is already on left side
        everything_on_left = str(left_side)
    else:
        if right_side[0] == "-" or right_side[0] == "+":
            # checks if the first argument on the right side has - or +, if it doesnt, then it adds one in the end
            additional_operator = ''
        else:
            additional_operator = '-'
        if "(" in right_side:
            # checks if there are any brackets
            right_side = getParensToLeft(right_side)
        elif "|" in right_side:
            # checks if there are any abs
            right_side = getAbsToLeft(right_side)
        else:
            right_side = "".join(getSignsReversed(right_side))
        everything_on_left = str("".join(left_side + additional_operator + right_side))
    return everything_on_left

def optimizeEquationForSympy(equation):
    equation = getMissingMultiplic(equation)
    equation = getAllToLeftSide(equation)
    return equation

if __name__ == '__main__':
    print(optimizeEquationForSympy('3x + 7 = 6y - p**(-4)'))
