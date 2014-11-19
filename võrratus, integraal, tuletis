# coding=utf-8
from sympy import *
x = symbols('x')

list_of_variables = ['q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p', 'ü', 'õ', 'a', 's', 'd', 'f', 'g', 'h', 'j',
                     'k', 'l', 'ö', 'ä', 'z', 'x', 'c', 'v', 'b', 'n', 'm', 'Q', 'W', 'E', 'R', 'T', 'Y', 'U', 'I',
                     'O', 'P', 'Ü', 'Õ', 'A', 'S', 'D', 'F', 'G', 'H', 'J', 'K', 'L', 'Ö', 'Ä', 'Z', 'X', 'C', 'V',
                     'B', 'N', 'M']


def getVariableNamesChanged(at_first, expression, after):  # changes variable names
    expression = list(expression)
    for i in range(len(expression)):
         if expression[i] == at_first:
            expression[i] = after
    return "".join(expression)


def getStringsRemoved(argument):  # removes strings from argument, so there are only numbers and minuses
    rem = []
    for el in argument:
        if el.isdigit() is False and el != "-" and el != ".":
            rem.append(el)
    for i in range(len(rem)):
        argument.remove(rem[i])
    return argument


def getMinusToPlusMinus(argument):  # changes - to +-
    for i in range(len(argument)):
        if argument[i] == "-":
            argument[i] = "+-"
    return argument


def getOperatorsChanged(argument):  # changes - to + and + to +-
    for i in range(len(argument)):
        if argument[i] == "-":
             argument[i] = "+"
        elif argument[i] == "+":
             argument[i] = "+-"
    return argument


def getRidOfSpaces(argument):  # gets rid of the spaces inside the argument
    argument = argument.split(" ")
    argument = "".join(argument)
    return argument


def getAbsWithoutOperatorsChanges(right_side):  # changes operators on the right side, if there are abs
    right_side = list(right_side)
    between_abs = []
    for i in range(len(right_side)):
        if right_side[i] == "|":
            between_abs.append(i)  # appends abs indexes into list
    abs = right_side[between_abs[0]:between_abs[1]+1]  # doesn't switch operators between abs
    return "".join(getOperatorsChanged(right_side[:between_abs[0]])) + "".join(getMinusToPlusMinus(abs)) + \
           "".join(getOperatorsChanged(right_side[between_abs[1]+1:]))


def getBracketsWithoutOperatorsChanges(right_side):  # changes operators on the right side if there are brackets
    first = []
    second = []
    counter = 0
    for i in range(len(right_side)):
        if right_side[i] == "(" or right_side[i] == ")":
            if right_side[i] == "(":
                if counter == 0:
                    first.append(i)  # appends the first bracket to list
                counter += 1  # counts opened brackets
            else:
                counter -= 1  # if there is an closing bracket, it subtracts on from counter
                if counter == 0:  # and once the counter hits 0, it appends the index of ending bracket to the list
                    second.append(i)
    between_brackets = []
    for i in range(len(first)):
        between_brackets.append(right_side[first[i]:second[i]+1])  # appends the area between brackets into list
    brackets = []  # adds brackets and the after brackets part until the last brackets
    for i in range(len(between_brackets)-1):
        bracket = "".join(getMinusToPlusMinus(between_brackets[i]))
        brackets.append(bracket)
        after_bracket = "".join(getOperatorsChanged(right_side[int(second[i]+1):int(first[i+1])]))
        brackets.append(after_bracket)
    brackets_ = "".join(brackets)
    beginning = "".join(getOperatorsChanged(right_side[:int(first[0])]))
    last_bracket = "".join(getMinusToPlusMinus(between_brackets[-1]))
    end = "".join(getOperatorsChanged(right_side[int(second[-1]+1):]))
    right_side = beginning + brackets_ + last_bracket + end  # adds the beginning, the first brackets with the area
    return right_side  # between them, last bracket and the ending


#Everything on one side
def getEverythingOnOneSideAsString(argument):  # takes an argument as string and returns the it
    argument = list(getRidOfSpaces(argument))  # with all arguments on the left side with operators changed
    equal_sign = argument.index("=")
    left_side = argument[:equal_sign]
    left_side = "".join(getMinusToPlusMinus(left_side))
    right_side_beginning = equal_sign+1
    right_side = argument[right_side_beginning:]  # list of the things on the right side
    if right_side == ["0"]:  # checks if maybe everything is already on left side
        everything_on_left = str(left_side)
    else:
        if right_side[0] == "-" or right_side[0] == "+":  # checks if the first argument on the right
            additional_operator = "".join([])  # side has - or +, if it doesnt, then it adds
        else:                                     # one in the end
            additional_operator = "".join(["+-"])
        if "(" in right_side:  # checks if there are any brackets
            right_side = getBracketsWithoutOperatorsChanges(right_side)
        elif "|" in right_side:  # checks if there are any abs
            right_side = getAbsWithoutOperatorsChanges(right_side)
        else:
            right_side = "".join(getOperatorsChanged(right_side))
        everything_on_left = str("".join(left_side + additional_operator + right_side))  # add left and right sides
    return everything_on_left


#Multiplication marks
def getMissingMultiplicationMarks(argument):  # if there are any missing multiplication mark in the input, it adds
    argument = list(getRidOfSpaces(argument))
    for i in range(len(argument)-1):
        if (argument[i]).strip().isdigit() is True:
            if argument[i+1] in list_of_variables:
                argument.insert(i+1, "*")   # between number and letter
            elif argument[i+1] == "(":
                argument.insert(i+1, "*")  # between number and (
        elif argument[i] == ")":
            if argument[i+1] == "(":
                argument.insert(i+1, "*")  # between brackets
            elif (argument[i+1]).strip().isdigit() is True:
                argument.insert(i+1, "*")  # between ) and a number
            elif argument[i+1] in list_of_variables:
                argument.insert(i+1, "*")  # between ) and letter
        elif argument[i] in list_of_variables:
            if (argument[i+1]).strip().isdigit() is True:
                argument.insert(i+1, "*")  # between letter and number
            elif argument[i+1] == "(":
                argument.insert(i+1, "*")  # between letter and (
    return "".join(argument)


def getInputOrganized(argument):  # changes operators, takes everything on one side and adds missing * marks
    return getMissingMultiplicationMarks(getEverythingOnOneSideAsString(argument))


#Inequalities
def getInequalitiesSolved(inequalitie):
    result = str(solve(getMissingMultiplicationMarks(inequalitie)))
    if result is "False":
        result = "Lahendid puuduvad"
    else:
        im_index = result.index("im")
        variable = result[im_index + 3]
        result = getVariableNamesChanged(variable, result, "x")  # changes variable to "x"
        if result == "im(x) == 0":
            result = "Lahendiks sobivad kõik reaalarvud"
        else:
            result = result[4:-1]  # removes the first "and" that comes with imaginary result
            separate_results = result.split(",")
            to_remove = []
            for el in separate_results:
                if "im" in el:
                    to_remove.append(el)
            for el in to_remove:
                separate_results.remove(el)  # removes imaginary results
            result = ",".join(separate_results)
            if result[:2] == "Or":  # conjuction = "või"
                result = result[3:]
            elif result[:3] == "And":  # conjuction = "ja"
                result = result[4:]
            for i in range(len(result)-12):
                if result[i:i+12] == "re(x), re(x)":  # writes results, that are between intervals together
                    result = "".join(result[:i] + "x" + result[i+12:])
            result = " või".join(result.split(","))  # replaces "," with "or"
            for i in range(len(result)-5):
                if result[i:i+3] == "And":
                    result = "".join(result[:i] + result[i+3:])  # deletes unwanted "And"-s
                elif result[i:i+5] == "re(x)":
                    result = "".join(result[:i] + "x" + result[i+5:])  # from re(x) keeps only x
            if result[0] == "(":
                result = result[1:]  # deletes the first unnecessary bracket
            if "sqrt" not in result:
                if result[-1] == ")":
                    result = result[:-1]  # removes the last unnecessary bracket
                for i in range(len(result)-1):
                    if result[i:i+1] == ")" or result[i:i+1] == "(":  # deletes all brackets
                        result = "".join(result[:i] + result[i+1:])
            result = "".join(result)
            if result[-1] == ")" and result[-2] == ")":  # deletes the unnecessary bracket from ending
                result = result[:-1]
    result = getVariableNamesChanged("x", result, variable).strip()
    return result


#Integral
def getExpressionIntegrated(expression):
    d_index = expression.index("d")  # separating the integration part from the lanes part
    integral = list(getMissingMultiplicationMarks((expression[:d_index]).strip()))
    variable = expression[d_index + 1]
    integral = getVariableNamesChanged(variable, integral, "x")
    after_integral = (expression[d_index + 2:]).strip()
    if after_integral == "":
        result = str(integrate(integral, x))
    else:
        if "," in after_integral:  # if lanes are separated with commas
            a = list(after_integral.split(",")[0].strip())
            b = list(after_integral.split(",")[1].strip())
        else:
            spaces = after_integral.count(" ")  # if lanes are written down with words, counts spaces
            if spaces == 1:
                a = list(after_integral.split(" ")[0].strip())  # for example 2-st 5-ni
                b = list(after_integral.split(" ")[1].strip())
            elif spaces == 3:
                a = list(after_integral.split(" ")[1])  # for examole from 3 to 9
                b = list(after_integral.split(" ")[3])
        a = float("".join(getStringsRemoved(a)))
        b = float("".join(getStringsRemoved(b)))
        result = str(integrate(integral, (x, a, b)))
    result = getVariableNamesChanged("x", result, variable)  # changes variable name back to what it was
    try:
        result = round(float(result), 2)
    except:
        result = result
    return result


#Derivative
def getDerivativeVariable(expression):
    expression = list(expression)
    list_of_not_variables_in_derivative = ["a", "e", "c", "o", "s", "i", "n", "t", "l", "r", "g", "h"]
    for i in range(len(expression)):
        if expression[i] in list_of_variables and expression[i] not in list_of_not_variables_in_derivative:
            return expression[i]


def getExpressionDerivative(expression):
    variable = getDerivativeVariable(expression)
    expression = list(expression)
    for i in range(len(expression)-1):
        if (expression[i]).strip().isdigit() is True and expression[i+1] in list_of_variables:
            expression.insert(i+1, "*")   # inserts multiplication mark between number and letter
        elif expression[i] == ")" and expression[i+1] == "(":
            expression.insert(i+1, "*")  # insert multiplication mark between two brackets
    expression = getVariableNamesChanged(variable, "".join(expression), "x")
    result = str(diff(expression, x))
    result = getVariableNamesChanged("x", result, variable)
    return result



# selle funktsiooniga saab viia kõik ühele poole ja lisada korrutusmärgid
#print(getInputOrganized("x+3-2=-4+3|-x-7|+4-2"))
#print(getInputOrganized("x+3-2=4-2"))
#print(getInputOrganized("-3=2+2x(-4+3)-2"))

# võrratused
#print(solve(x**2 > -1))
#print(getInequalitiesSolved("t > 2"))
#print(getInequalitiesSolved("(x-1)*(x-2)*(x-3)*(x-4) > 0"))
#print(solve((x-1)*(x-2)*(x-3)*(x-4)*(x-5) > 0))
#print(getInequalitiesSolved("(x-1)(x-2)(x-3)(x-4)(x-5) > 0"))
#print(getInequalitiesSolved("x**3 > x"))

# integraal
#print(getExpressionIntegrated("2y dy from 3 to 5"))
#print(getExpressionIntegrated("(x**2 + 2x)dx  3st 5ni"))
#print(getExpressionIntegrated("2x dx (2,9)"))
#print(getExpressionIntegrated("2y dy"))
#print(getExpressionIntegrated("(x**2 + 2x)dx  3.4st 5ni"))

# tuletis
#print(getExpressionDerivative("x**2"))
#print(getExpressionDerivative("2x"))
#print(getExpressionDerivative("sin(x)"))
