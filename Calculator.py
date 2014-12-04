import sympy
#x = sympy.symbols("x") # Milleks seda vaja?


def calculator(raw_expr, round_to="3"):
    raw_expr = ''.join(raw_expr).strip()
    round_to = sympy.sympify(round_to)
    expr = sympy.sympify(raw_expr)
    answer = str(expr.evalf(round_to))
    if raw_expr == answer:
        raise SyntaxError
    print(answer.rstrip(('.')))  # DB
    return answer.rstrip('.')

if __name__ == '__main__':
    print(calculator("log(2)**2 - 6*x/sqrt(17)", "7"))
    print(calculator("log(3)", '6'))
    print(calculator("ilm T7*y - 30"))
