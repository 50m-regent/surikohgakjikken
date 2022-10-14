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
    for dt, num in [[0.1, '1'], [0.01, '01'], [0.001, '001'], [0.0001, '0001']]:
        plt.plot(*readfile(f'solve{num}.txt'), label=f'$\Delta t={dt}$')
        
    t = np.linspace(0, 20)
    a = 2
    u0 = 1
    b = 1
    C = u0 - b / a
    plt.plot(t, C * np.exp(-a * t) + b / a, label='$u(t)$')
    
    plt.xlabel('$t$')
    plt.ylabel('$u$', rotation=0)
    
    # plt.xscale('log')
    # plt.yscale('log')
    
    plt.xlim(0, 20)
    plt.ylim(-3, 3)
    
    plt.legend()
    
    plt.savefig('kadai5.eps')
    