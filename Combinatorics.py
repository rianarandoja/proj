from sympy import factorial

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

#print(getFact("7!"))
#print(solveCombinations("3C 2"))
#print(solvePermutations("4V4"))
