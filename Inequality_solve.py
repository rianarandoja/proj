from Equation_manipulation import *
from sympy import *
from tkinter import *
x = symbols("x")

def InEqResultWindow(result, user_input="user input"):
    root = Tk()
    root.title("Aafrika")

    y_scrollbar = Scrollbar(root)
    y_scrollbar.pack(side=RIGHT, fill=Y)

    listbox = Listbox(root, yscrollcommand=y_scrollbar.set, selectmode=MULTIPLE, height=6, width=50,
                      selectbackground="gold2", activestyle="none")
    listbox.pack(side=LEFT, fill=BOTH, expand=1)

    y_scrollbar.config(command=listbox.yview)

    listbox.insert(0, "")
    listbox.insert(1, " "*30 + user_input)
    listbox.insert(2, "")

    for item in result:
        if item != "":
            listbox.insert(END, str("           •   " + item.strip()))

    root.mainloop()

def solveInequality(inequality):
    inequality = "".join(inequality)
    inequality = optimizeEquationForSympy(inequality)
    try:
        result = str(solve(inequality))
    except PolynomialError:
        return -1
    result = optimizeEquationForSympy(result)
    try:
        result = round(float("".join(result[1:-1])), 2)
    except ValueError:
        if result == 'False':
            result = ["Lahendid puuduvad"]
        else:
            im_index = result.index("im")
            variable = result[im_index + 4]
            result = result.replace(variable, "x")
            if result == "im(x) == 0" or result == "im*(x)-=0":
                result = ["Lahendiks sobivad kõik reaalarvud"]
            else:
                # removes imaginary results
                separate_results = result.split(",")
                to_remove = []
                for el in separate_results:
                    if "im" in el:
                        to_remove.append(el)
                    elif "RootOf" in el:
                        to_remove.append(el)
                for el in to_remove:
                    separate_results.remove(el)
                result = ",".join(separate_results)
                result = (result.replace('re(x),re(x)', ' x ')
                                .replace(',', ' või')
                                .replace('And', '')
                                .replace('re(x)', ' x ')
                                .replace("Or", ""))
                if "**0.5" not in result:
                    result = (result.replace('(', '')
                                    .replace(')', ''))
                result = result.replace("x", variable).strip().replace("*", "")
                result = result.replace("(", "").replace(")", "")
                result = result.replace("<", " < ").replace(">", " > ")
                result = result.split(" või ")
    return result

def Inequality(user_input):
    user_input = "".join(user_input)
    result = solveInequality(user_input)
    if result == -1:
        return -1
    InEqResultWindow(result, user_input)


if __name__ == '__main__':
    print(Inequality(["(x-4)(5+x)(x-2)<0"]))
    print(Inequality("(x)**0.5-1 > 0 "))
