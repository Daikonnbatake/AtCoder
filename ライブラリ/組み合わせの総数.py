import math
def combination(n,r):
    return math.factorial(n) // (math.factorial(n - r) * math.factorial(r))