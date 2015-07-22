#!/bin/python

import primes
import random, timeit, json, math

def random_odd_number(min_bits, max_bits):
    bits = random.SystemRandom().randrange(min_bits, max_bits)
    min_val = pow(2, bits) + 1
    max_val = pow(2, bits + 1) - 1
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

def write_to_file(times, reference_function, name, filename):
    f = open(filename, 'w')
    reference = create_reference_data(times, reference_function)
    json.dump({'name': name, 'data': times, 'reference_data': reference}, f)
    f.close()

def create_reference_data(times, function):
    mid = times[len(times)//2]
    # get a constant to produce a nice reference
    constant = mid[1] / function(mid[0])
    return [(point[0], constant * function(point[0])) for point in times]

def sqrt_bits(bits):
    return math.sqrt(math.pow(2,bits))

def log_cubed_bits(bits):
    return math.pow(bits, 3) # log(2^bits) = bits

SAMPLES  = 3000

trial_division   = benchmark('Trial Division', primes.trial_division, lambda: random_odd_number(10, 40), SAMPLES)
MIN_BITS = 512
MAX_BITS = 1024
miller_rabin     = benchmark('Miller-Rabin', primes.miller_rabin, lambda: random_odd_number(MIN_BITS, MAX_BITS), SAMPLES)
solovay_strassen = benchmark('Solovay-Strassen', primes.solovay_strassen, lambda: random_odd_number(MIN_BITS, MAX_BITS), SAMPLES)

write_to_file(trial_division, sqrt_bits, 'Trial Division','trial_division.plot')
write_to_file(miller_rabin, log_cubed_bits, 'Miller-Rabin', 'miller_rabin.plot')
write_to_file(solovay_strassen, log_cubed_bits, 'Solovay-Strassen', 'solovay_strassen.plot')
