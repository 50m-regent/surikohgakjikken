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
    ts2, us2 = readfile('laurents2.txt')
    ts4, us4 = readfile('laurents4.txt')
    ts6, us6 = readfile('laurents6.txt')
    plt.plot(ts2, us2, label='$n=2$')
    plt.plot(ts4, us4, label='$n=4$')
    plt.plot(ts6, us6, label='$n=6$')
    
    ts2s, us2s = [], []
    umax = -float('inf')
    for t, u in zip(ts2, us2):
        if t < 1:
            continue
        
        if u > umax:
            ts2s.append(t)
            us2s.append(u)
            umax = u
    
    t = np.logspace(0, 2)
    plt.plot(t, 1e-17 * t ** 15, linestyle='--', label='$10^{-17}t^{15}$', color='grey')
    plt.plot(t, 1e-19 * t ** 15, linestyle=':', label='$10^{-19}t^{15}$', color='grey')
    plt.plot(t, 1e-21 * t ** 15, linestyle='-.', label='$10^{-21}t^{15}$', color='grey')
    
    # plt.scatter(ts2s, us2s)
    
    plt.xlabel('$t$')
    plt.ylabel('$\Delta_n$', rotation=0)
    
    plt.yscale('log')
    
    plt.xlim(0.01, 100)
    plt.ylim(10 ** -6.5, 100)
    
    plt.legend()
    
    # plt.savefig('2halflog.eps')
    
    plt.xscale('log')
    plt.savefig('2fulllog.eps')
    