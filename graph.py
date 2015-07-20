#!/bin/python

import sys
import json
import matplotlib.pyplot as plt

def read_from_file(name):
    f = open(name, 'r')
    times = json.load(f)
    f.close()
    return times

def create_graph(name, times):
    x = []
    y = []
    max_x =0
    max_y = 0
    min_x = sys.maxsize
    for i in times:
        x.append(i[0])
        y.append(i[1])
        max_x = max(max_x, i[0])
        min_x = min(min_x, i[0])
        max_y = max(max_y, i[1])
    plt.title(name)
    plt.xlabel('nbr of bits')
    plt.ylabel('duration (secs)')
    plt.axis([min_x * 0.95, max_x * 1.05, 0 - max_y * 0.05, max_y * 1.05])
    plt.plot(x, y, 'ro')
    plt.show()

if len(sys.argv) == 3:
    create_graph(sys.argv[1], read_from_file(sys.argv[2]))
else:
    print(len(sys.argv))
    print('This is not the chart you are looking for o_O')

