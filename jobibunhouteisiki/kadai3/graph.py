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
    plt.plot(*readfile('euler.txt'), color='black', zorder=1, label='FE', marker='.')
    plt.plot(*readfile('adams_second.txt'), color='red', zorder=2, label='AB2', marker='v')
    plt.plot(*readfile('adams_third.txt'), color='blue', zorder=3, label='AB3', marker='^')
    plt.plot(*readfile('heun.txt'), color='green', zorder=4, label='H', marker='s')
    plt.plot(*readfile('runge_kutta.txt'), color='gold', zorder=5, label='RK', marker='d')
    
    t = np.logspace(-8, 10)
    plt.plot(t, t, zorder=0, color='grey', linestyle='-', label='$\Theta (\Delta t)$')
    plt.plot(t, 0.7 * t ** 2, zorder=0, color='grey', linestyle='--', label='$\Theta (\Delta t^2)$')
    plt.plot(t, 0.7 * t ** 3, zorder=0, color='grey', linestyle='-.', label='$\Theta (\Delta t^3)$')
    plt.plot(t, 0.01 * t ** 4, zorder=0, color='grey', linestyle=':', label='$\Theta (\Delta t^4)$')
    
    plt.xlabel('$\Delta t$')
    plt.ylabel('$E$', rotation=0)
    
    plt.xscale('log')
    plt.yscale('log')
    
    plt.xlim(1e-7, 1)
    plt.ylim(1e-15, 1)
    
    plt.legend(ncol=2, loc='upper left')
    
    plt.tight_layout()
    
    plt.savefig('kadai3.eps')
    