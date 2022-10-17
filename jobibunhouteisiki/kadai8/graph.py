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
    plt.plot(*readfile('R100.txt'))
    plt.plot(*readfile('R1000.txt'))
    
    plt.xlabel('$K$')
    plt.ylabel(r'$\bar{R}$', rotation=0)
    
    # plt.xscale('log')
    # plt.yscale('log')
    
    plt.xlim(1, 3)
    # plt.ylim(-3, 3)
    
    # plt.legend()
    
    plt.savefig('8.eps')
    