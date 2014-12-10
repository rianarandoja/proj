from sympy import *
from tkinter import *

def calculator(raw_expr, round_to="3"):
    raw_expr = (''.join(raw_expr)).strip()
    round_to = sympify(round_to)
    if "C" or "V" in raw_expr:
        list_ = []
        if "+" not in raw_expr and "-" not in raw_expr:
            list_.append(raw_expr)
        else:
            for i in range(len(raw_expr)):
                if "+" not in raw_expr and "-" not in raw_expr:
                    list_.append(raw_expr[:])
                    break
                elif raw_expr[i] in ["+", "-", "*", "/"]:
                    list_.append(raw_expr[:i])
                    list_.append(raw_expr[i])
                    raw_expr = raw_expr[i+1:]
        for i in range(len(list_)):
            if "C" in list_[i]:
                list_[i] = str(solveCombinations(list_[i]))
            elif "V" in list_[i]:
                list_[i] = str(solvePermutations(list_[i]))
            else:
                pass
        expr = sympify("".join(list_))
    else:
        expr = sympify(raw_expr)
    answer = str(expr.evalf(round_to))
    if raw_expr == answer:
        raise SyntaxError
    print(answer.rstrip(('.')))  # DB
    answer = answer.rstrip('.')
    return answer

def solveCombinations(combination):
    n = int(combination[:combination.index("C")].strip())
    r = int(combination[combination.index("C")+1:].strip())
    result = factorial(n)/(factorial(r)*factorial(n-r))
    return result

def solvePermutations(permutation):
    n = int(permutation[:permutation.index("V")].strip())
    r = int(permutation[permutation.index("V")+1:].strip())
    result = factorial(n)/factorial(n-r)
    return result

def Calc(raw_expr):

    raw_expr = "".join(raw_expr)

    result = calculator(raw_expr)

    calc_win = Tk()
    calc_win.title("Aafrika")
    listbox = Listbox(calc_win, selectmode=MULTIPLE, height=6, width=50, selectbackground="gold2", activestyle="none")
    listbox.pack(side=LEFT, fill=BOTH, expand=1)

    listbox.insert(0, "")

    listbox.insert(1, " "*20 + "".join(raw_expr))
    listbox.insert(2, "")

    if isinstance(result, str):
        listbox.insert(END, str("      •   " + result.strip()))

    else:
        for item in result:
            listbox.insert(END, str("      •   " + item.strip()))

    listbox.insert(END, "")

    calc_win.mainloop()


if __name__ == '__main__':
    Calc(["log(2)**2 - 6*x/sqrt(17)"])
    Calc("3!")
    #calculatorResult("ilm T7*y - 30")
    Calc("5! + 4V2 + 3C2")
