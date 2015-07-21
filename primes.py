import math, random

# Primality test functions. Assume that "n" is odd and greater than 3.

# Tests if 'n' is prime by trial division, by checking if it has a factor
# k (1 < k <= sqrt(n))
def trial_division(n):
    return not(any(n % x == 0 for x in range(3, math.floor(math.sqrt(n))+1)))

# Tests if 'n' is a strong pseudoprime using the Miller-Rabin probabilistic algorithm.
#
# The following properties assume that 'n' is prime (if a property fails, then we
# know 'n' is composite).
#
# Randomly picks 'rounds' bases.
# For each base 'a', start with Fermat's little theorem (a^(n-1) = 1 (mod n)).
#  Take the square root of 1 (in a finite field Z/nZ, assuming n is prime)
#  and verify that every root is either 1 or -1.
#  so, (suppose n-1 = 2^s * d (d odd) and n prime), we have EITHER:
#  - a^d = 1 (mod n) (no need to continue, will give 1 for the 's' time that we'll square it)
#  - a^(2^r * d) = -1 (mod n), for a certain r in [0,s-1] (all subsequent squarings will
#    then give 1, so we can stop there).
#  The contrapositive:
#  n is composite if we have BOTH:
#  - a^d != 1 (mod n)
#  - a^(2^r * d) != -1 (mod n), for all r in [0,s-1]
#
# Has a probability of 4^(-'rounds') to return a composite number as a strong pseudoprime.
def miller_rabin(n, rounds = 40):
    # get the form n - 1 = 2^s * d
    s = 0
    d = n-1
    while is_even(d):
        d //= 2
        s += 1

    for i in range(rounds):
        a = random.randrange(2,n)
        x = pow(a, d, n)
        if x == 1: # pseudoprime
            continue
        skip = False
        for r in range(s):
            if x == n-1: # pseudoprime
                skip = True
                break
            x = pow(x, 2, n)

        if not skip:
            return False # composite

    return True

def solovay_strassen(n, rounds = 80):
    return False #TODO


def is_even(n):
    return n & 1 == 0
