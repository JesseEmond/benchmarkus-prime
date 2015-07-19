#!/bin/python

import primes
import random

def random_odd_number(min_bits, max_bits):
    min_val = pow(2,min_bits - 1) + 1
    max_val = pow(2,max_bits) + 1
    return random.SystemRandom().randrange(min_val, max_val, 2)


def time_function_call(callback):
    callback()
    return 5 # TODO actually time the call to the function and return the desired statistic

def benchmark(name, callback, samples):
    print()
    print('starting benchmark for "', name, '":')

    times = [time_function_call(callback) for i in range(samples)]

    print('end of benchmark for "', name, '".')
    print()

    return times

def make_prime_test_callback(primality_test, min_bits, max_bits):
    return lambda: primality_test(random_odd_number(min_bits, max_bits))





SAMPLES  = 1
MIN_BITS = 512
MAX_BITS = 1024

trial_division   = benchmark('Trial Division', make_prime_test_callback(primes.trial_division, MIN_BITS, MAX_BITS), SAMPLES)
miller_rabin     = benchmark('Miller-Rabin', make_prime_test_callback(primes.miller_rabin, MIN_BITS, MAX_BITS), SAMPLES)
solovay_strassen = benchmark('Solovay-Strassen', make_prime_test_callback(primes.solovay_strassen, MIN_BITS, MAX_BITS), SAMPLES)

# TODO output data to file for graph-generator to use?
