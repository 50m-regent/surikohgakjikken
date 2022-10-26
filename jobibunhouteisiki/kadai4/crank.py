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
    t = np.linspace(0, 5)
    a = 10
    u0 = 1
    b = 1
    C = u0 - b / a
    plt.plot(t, C * np.exp(-a * t) + b / a, label='$u(t)$', color='black')
    
    markers = {
        0.1: '.',
        0.3: 'v',
        0.5: 's'
    }
    colors = {
        0.1: 'red',
        0.3: 'blue',
        0.5: 'green'
    }
    for dt in [0.1, 0.3, 0.5]:
        plt.plot(*readfile(f'crank{str(dt)[2:]}.txt'), label=f'$\Delta t={dt}$', marker=markers[dt], color=colors[dt])
    
    plt.xlabel('$t$')
    plt.ylabel('$u$', rotation=0)
    
    # plt.xscale('log')
    # plt.yscale('log')
    
    plt.xlim(0, 5)
    # splt.ylim(, 5)
    
    plt.legend()
    
    plt.tight_layout()
    
    plt.savefig('crank.eps')
    # plt.show()
    