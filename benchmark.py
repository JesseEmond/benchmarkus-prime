#!/bin/python

import primes
import random
import timeit
import json

def random_odd_number(min_bits, max_bits):
    min_val = pow(2,min_bits - 1) + 1
    max_val = pow(2,max_bits) + 1
    return random.SystemRandom().randrange(min_val, max_val, 2)


def time_function_call(test):
    values = test()
    timer = timeit.Timer(values[0])

    return (values[1].bit_length(), timer.timeit(1))

def benchmark(name, test, samples):
    print()
    print('starting benchmark for "', name, '":')

    times = [time_function_call(test) for i in range(samples)]

    print('end of benchmark for "', name, '".')
    print()

    return times

def make_prime_test(primality_test, min_bits, max_bits):
    def generate():
        odd_number = random_odd_number(min_bits, max_bits)
        return (lambda: primality_test(odd_number), odd_number)

    return generate

def write_to_file(times, name):
    f = open(name, 'w')
    json.dump(times, f)
    f.close()

SAMPLES  = 1
MIN_BITS = 512
MAX_BITS = 1024

trial_division   = benchmark('Trial Division', make_prime_test(primes.trial_division, MIN_BITS, MAX_BITS), SAMPLES)
miller_rabin     = benchmark('Miller-Rabin', make_prime_test(primes.miller_rabin, MIN_BITS, MAX_BITS), SAMPLES)
solovay_strassen = benchmark('Solovay-Strassen', make_prime_test(primes.solovay_strassen, MIN_BITS, MAX_BITS), SAMPLES)

write_to_file(trial_division, 'trial_division')

# TODO output data to file for graph-generator to use?
