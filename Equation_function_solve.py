from Equation_manipulation import isVariable
from sympy import *
from Equation_manipulation import optimizeEquationForSympy
from Function_differentiation import solveDiff
from Inequality_solve import solveInequality
from Function_inspection import funcInspect
from tkinter import *
import tkinter.ttk as ttk

x = symbols("x")

def solveEquationArgsHandler(args):
    if '=' in ''.join(args):
        return True
    return False

def solveEquation(equation):
    equation = "".join(equation)
    equation = ''.join(equation)
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

    output = output.strip().split("\n")
    return output

def solveFunction(function):
    function = "".join(function)
    output = []
    nullkohad = "Nullkohad: " + " ,  ".join(solveEquation(function)).strip().strip(",")
    positiivsuspiirkond = "Positiivsuspiirkond: " + " , ".join(solveInequality(str(function + "> 0")))
    negatiivsuspiirkond = "Negatiivsuspiirkond: " + " , ".join(solveInequality(str(function + "< 0")))
    ekstreemumid = solveEquation(solveDiff(function))
    if len(ekstreemumid) > 1:
        x_1 = round(float(ekstreemumid[0][6:]), 2)
        y_1 = round(eval(function.replace("x", str(x_1))), 2)
        x_2 = round(float(ekstreemumid[1][6:]), 2)
        y_2 = round(eval(function.replace("x", str(x_2))), 2)
        if y_1 > y_2:
            maks = "Maksimumpunkt (" + str(x_1) + ", " + str(y_1) + ")"
            min = "Miinimumpunkt (" + str(x_2) + ", " + str(y_2) + ")"
        else:
            maks = "Maksimumpunkt (" + str(x_2) + ", " + str(y_2) + ")"
            min = "Miinimumpunkt (" + str(x_1) + ", " + str(y_1) + ")"
        output.append(min)
        output.append(maks)
    else:
        ekstreemumid = ("Ekstreemumpunkt (" + "".join(ekstreemumid[0][6:]) + ", " +
                        str(sympify(function.replace("x", (ekstreemumid[0][5:].strip(")")))).evalf(2)) + ")")
        output.append(ekstreemumid)
    kasvamisvahemik = "Kasvamisvahemik: " + " ,  ".join(solveInequality(str(solveDiff(function) + "> 0")))
    kahanemisvahemik = "Kahanemisvahemik: " + " ,  ".join(solveInequality(str(solveDiff(function) + "< 0")))
    try:
        käänukohad = "Käänukohad: " + " ,  ".join(solveEquation(solveDiff(solveDiff(function))))
        kumerusvahemik = ("Kumerusvahemik: " + " ,  ".join(solveInequality(str(solveDiff(solveDiff(function))
                                                                               + "< 0"))))
        nõgususvahemik = ("Nõgususvahemik: " + " ,  ".join(solveInequality(str(solveDiff(solveDiff(function))
                                                                               + "> 0"))))
        return [nullkohad] + output + [positiivsuspiirkond, negatiivsuspiirkond, kasvamisvahemik, kahanemisvahemik,
                käänukohad, nõgususvahemik, kumerusvahemik]
    except UnboundLocalError:
        return [nullkohad] + output + [positiivsuspiirkond, negatiivsuspiirkond, kasvamisvahemik, kahanemisvahemik]

def Function(user_input):

    user_input = "".join(user_input)

    optimized_result = optimizeEquationForSympy(user_input.replace("y=", "")).replace("-0", "")

    result = solveFunction(optimized_result)

    root = Tk()
    root.title("Aafrika")

    y_scrollbar = Scrollbar(root)
    y_scrollbar.pack(side=RIGHT, fill=Y)

    listbox = Listbox(root, yscrollcommand=y_scrollbar.set, selectmode=MULTIPLE, height=7, width=50,
                      selectbackground="gold2", activestyle="none")
    listbox.pack(side=LEFT, fill=BOTH, expand=1)

    y_scrollbar.config(command=listbox.yview)

    draw_function_input = ["y=" + optimized_result]

    button = (ttk.Button(root, text="√Joonista!", width=10, command=lambda: funcInspect(draw_function_input)))
    button.place(x=190, y=13)

    listbox.insert(0, "")
    listbox.insert(1, " "*20 + "".join(draw_function_input))
    listbox.insert(2, "")

    for item in result:
        listbox.insert(END, str("      •   " + item.strip()))

    listbox.insert(END, "")

    root.mainloop()

def resultWindowForEquatation(result, user_input):
    root = Tk()
    root.title("Aafrika")

    y_scrollbar = Scrollbar(root)
    y_scrollbar.pack(side=RIGHT, fill=Y)

    listbox = Listbox(root, yscrollcommand=y_scrollbar.set, selectmode=MULTIPLE, height=6, width=50,
                      selectbackground="gold2", activestyle="none")
    listbox.pack(side=LEFT, fill=BOTH, expand=1)

    y_scrollbar.config(command=listbox.yview)

    button = (ttk.Button(root, text="√Kuva funktsioon!", width=17, command=lambda: Function(user_input)))
    button.place(x=185, y=13)

    listbox.insert(0, "")
    listbox.insert(1, " "*20 + user_input)
    listbox.insert(2, "")

    for item in result:
        if item != "":
            listbox.insert(END, str("           •   " + item.strip()))

    listbox.insert(END, "")

    root.mainloop()

def Equation(user_input):
    user_input = "".join(user_input)
    output = solveEquation(user_input)
    resultWindowForEquatation(output, user_input)

if __name__ == '__main__':
    #Function(["y=(x-4)(5+x)(4-x)"])
    Equation(["(x-4)(5+x)(4-x)=0"])
