import math

# Primality test functions. Assume that "n" is odd and greater than 3.

# Tests if 'n' is prime by trial division, by checking if it has a factor
# k such that 1<k<=sqrt(n)
def trial_division(n):
    return not(any(n % x == 0 for x in range(3, math.floor(math.sqrt(n))+1)))

def miller_rabin(n):
    return False #TODO

def solovay_strassen(n):
    return False #TODO
