from sympy import *
x = symbols("x")

def Calculator(expr, round_to="3"):
    round_to = sympify(round_to)
    expr = sympify(expr)
    answer = str(expr.evalf(round_to))
    if answer[-1] == ".":
        answer = answer[:-1]
    return answer

#print(Calculator("log(2)**2 - 6*x/sqrt(17)", "7"))
#rint(Calculator("17-3"))
#print(Calculator("6*17"))
