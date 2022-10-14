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
    t = np.linspace(0, 2)
    a = 10
    u0 = 1
    b = 1
    C = u0 - b / a
    plt.plot(t, C * np.exp(-a * t) + b / a, label='$u(t)$')
    
    for dt in [0.01, 0.05, 0.1, 0.5]:
        plt.plot(*readfile(f'crank{str(dt)[2:]}.txt'), label=f'$\Delta t={dt}$')
    
    plt.xlabel('$t$')
    plt.ylabel('$u$', rotation=0)
    
    # plt.xscale('log')
    # plt.yscale('log')
    
    plt.xlim(0, 5)
    # splt.ylim(, 5)
    
    plt.legend()
    
    # plt.savefig('heun.eps')
    plt.show()
    