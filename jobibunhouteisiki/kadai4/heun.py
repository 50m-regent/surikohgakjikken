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
    t = np.linspace(0, 2)
    a = 10
    u0 = 1
    b = 1
    C = u0 - b / a
    plt.plot(t, C * np.exp(-a * t) + b / a, label='$u(t)$', color='black')
    
    markers = {
        0.05: '.',
        0.15: 'v',
        0.21: 's'
    }
    colors = {
        0.05: 'red',
        0.15: 'blue',
        0.21: 'green'
    }
    for dt in [0.05, 0.15, 0.21]:
        plt.plot(*readfile(f'heun{str(dt)[2:]}.txt'), label=f'$\Delta t={dt}$', marker=markers[dt], color=colors[dt])
    
    plt.xlabel('$t$')
    plt.ylabel('$u$', rotation=0)
    
    # plt.xscale('log')
    # plt.yscale('log')
    
    plt.xlim(0, 3)
    plt.ylim(0, 4)
    
    plt.legend()
    
    plt.tight_layout()
    
    plt.savefig('heun.eps')
    # plt.show()
    