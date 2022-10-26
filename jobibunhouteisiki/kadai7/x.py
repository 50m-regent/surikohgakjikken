from matplotlib import pyplot as plt
import numpy as np

plt.rcParams["text.usetex"] = True
plt.rcParams["font.size"] = 18


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
    plt.plot(*readfile('x.txt'), color='black')
    
    plt.xlabel('$t$')
    plt.ylabel('$x$', rotation=0)
    
    # plt.xscale('log')
    # plt.yscale('log')
    
    plt.xlim(0, 100)
    plt.ylim(-20, 20)
    
    # plt.legend()
    plt.tight_layout()
    
    plt.savefig('x.eps')
    