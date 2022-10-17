from matplotlib import pyplot as plt
from matplotlib import rc
import numpy as np

rc('text', usetex=True)


def readfile(path):
    with open(path, 'r') as f:
        lines = f.read().splitlines()
        
    ts, us = [], []
    for line in lines:
        t, u = line.split()
        ts.append(float(t))
        us.append(float(u))
        
    return ts, us


if __name__ == '__main__':
    plt.plot(*readfile('x.txt'))
    
    plt.xlabel('$t$')
    plt.ylabel('$x$', rotation=0)
    
    # plt.xscale('log')
    # plt.yscale('log')
    
    plt.xlim(0, 100)
    # plt.ylim(-3, 3)
    
    # plt.legend()
    
    plt.savefig('x.eps')
    