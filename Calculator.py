import sympy
x = sympy.symbols("x")

def Calculator(expr, round_to="3"):
    round_to = sympy.sympify(round_to)
    expr = sympy.sympify(expr)
    answer = str(expr.evalf(round_to))
    return answer.rstrip('.')

if __name__ == '__main__':
    print(Calculator("log(2)**2 - 6*x/sqrt(17)", "7"))
    print(Calculator("log(3)", '6'))
    print(Calculator("6*17"))
