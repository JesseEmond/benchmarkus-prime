#!/bin/python

import primes
import random
import timeit
import json

def random_odd_number(min_bits, max_bits):
    min_val = pow(2,min_bits - 1) + 1
    max_val = pow(2,max_bits) + 1
    return random.SystemRandom().randrange(min_val, max_val, 2)


def time_function_call(test, rand):
    random_value = rand()
    timer = timeit.Timer(lambda: test(random_value))

    return (random_value.bit_length(), timer.timeit(1))

def benchmark(name, test, rand, samples):
    print()
    print('starting benchmark for "', name, '":')

    times = [time_function_call(test, rand) for i in range(samples)]

    print('end of benchmark for "', name, '".')
    print()

    return times

def write_to_file(times, name, filename):
    f = open(filename, 'w')
    json.dump({'name': name, 'data': times}, f)
    f.close()

SAMPLES  = 1
MIN_BITS = 512
MAX_BITS = 1024

trial_division   = benchmark('Trial Division', primes.trial_division, lambda: random_odd_number(MIN_BITS, MAX_BITS), SAMPLES)
#miller_rabin     = benchmark('Miller-Rabin', primes.miller_rabin, lambda: random_odd_number(MIN_BITS, MAX_BITS), SAMPLES)
#solovay_strassen = benchmark('Solovay-Strassen', primes.solovay_strassen, lambda: random_odd_number(MIN_BITS, MAX_BITS), SAMPLES)

write_to_file(trial_division, 'Trial Division','trial_division')

# TODO output data to file for graph-generator to use?
