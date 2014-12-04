from sympy import factorial

# Calculator arvutab faktoriaali ka, miks seda vaja?
def getFact(fact):
    return factorial(fact.replace("!", ""))

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
