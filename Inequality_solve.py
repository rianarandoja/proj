from Equation_manipulation import *
from sympy import solve
x = symbols("x")


def solveInequality(inequality):
    # solves inequalities, takes argument as string
    result = str(solve(getMissingMultiplic(inequality)))
    if result == 'False':
        result = "Lahendid puuduvad"
    else:
        im_index = result.index("im")
        variable = result[im_index + 3]
        result = result.replace(variable, "x")
        if result == "im(x) == 0":
            result = "Lahendiks sobivad kõik reaalarvud"
        else:
            result = result[4:-1]
            # removes the first "and" that comes with imaginary result
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
            result = (result.replace('re(x), re(x)', 'x')
                            .replace(',', ' või')
                            .replace('And', '')
                            .replace('re(x)', 'x')
                            .replace("Or", ""))
            if "sqrt" not in result:
                result = (result.replace('(', '')
                                .replace(')', ''))
            else:
                if result[-1] == ")" and result[-2] == ")":
                    # deletes the unnecessary bracket from ending
                    result = result[:-1]
                if result[0] == "(":
                    result = result[1:]
                    # deletes the first unnecessary bracket
        result = result.replace("x", variable).strip()
    return result

if __name__ == '__main__':
    print(solveInequality('4x-4 < 0'))
