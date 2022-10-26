from matplotlib import pyplot as plt
import numpy as np

plt.rcParams["text.usetex"] = True
plt.rcParams["font.size"] = 12


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
    colors = {
        0.1: 'red',
        0.01: 'green',
        0.001: 'blue',
        0.0001: 'yellow'
    }
    for dt, num in [[0.1, '1'], [0.01, '01'], [0.001, '001'], [0.0001, '0001']]:
        plt.plot(*readfile(f'solve{num}.txt'), label=f'$\Delta t={dt}$', color=colors[dt])
        
    t = np.linspace(0, 20, 1000)
    a = 2
    u0 = 1
    b = 1
    C = u0 - b / a
    plt.plot(t, C * np.exp(-a * t) + b / a, label='$u(t)$', color='black')
    
    plt.xlabel('$t$')
    plt.ylabel('$u$', rotation=0)
    
    # plt.xscale('log')
    # plt.yscale('log')
    
    plt.xlim(0, 14)
    plt.ylim(0, 1)
    
    plt.legend()
    plt.tight_layout()
    
    plt.savefig('kadai5.eps')
    