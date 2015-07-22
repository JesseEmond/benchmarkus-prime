#!/bin/python

import sys, json
import matplotlib.pyplot as plt

def read_from_file(name):
    f = open(name, 'r')
    times = json.load(f)
    f.close()
    return times

def create_graph(graph):
    x = []
    y = []
    for i in graph['data']:
        x.append(i[0])
        y.append(i[1])
    plt.title(graph['name'] + ' (log-log)')
    plt.xlabel('number (bits)')
    plt.ylabel('duration (secs) (log)')
    plt.yscale('log', basey=2)
    plt.plot(x, y, 'ro')
    plt.show()

if len(sys.argv) < 2:
    print('This is not the chart you are looking for o_O')
else:
    for i in range(1, len(sys.argv)):
        create_graph(read_from_file(sys.argv[i]))

