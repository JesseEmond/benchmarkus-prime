#!/bin/python

import primes

def random_odd_number(min_bits, max_bits):
    return 3 # TODO actually generate a random number with 'bits' bits with the first and last bit set to 1


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
