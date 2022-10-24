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


def plot_exp(ts2, us2, ts4, us4, ts6, us6):
    plt.cla()
    
    plt.plot(ts2, us2, label='$n=2$')
    plt.plot(ts4, us4, label='$n=4$')
    plt.plot(ts6, us6, label='$n=6$')
    
    t = np.logspace(0.8, 2)
    plt.plot(t, 2 ** (t - 15), linestyle='--', label='$2^{t - 15}$', color='black')
    plt.plot(t, 2 ** (t - 21), linestyle=':', label='$2^{t - 21}$', color='black')
    plt.plot(t, 2 ** (t - 27), linestyle='-.', label='$2^{t - 27}$', color='black')
    
    plt.xlabel('$t$')
    plt.ylabel('$\Delta_n$', rotation=0)
    
    plt.yscale('log')
    
    plt.xlim(0.01, 100)
    plt.ylim(10 ** -6.5, 100)
    
    plt.legend()
    
    plt.savefig('2halflog_exp.eps')
    
    plt.xscale('log')
    plt.savefig('2fulllog_exp.eps')



def plot_power(ts2, us2, ts4, us4, ts6, us6):
    plt.cla()
    
    plt.plot(ts2, us2, label='$n=2$')
    plt.plot(ts4, us4, label='$n=4$')
    plt.plot(ts6, us6, label='$n=6$')
    
    t = np.logspace(0, 2)
    plt.plot(t, 1e-17 * t ** 15, linestyle='--', label='$10^{-17}t^{15}$', color='black')
    plt.plot(t, 1e-19 * t ** 15, linestyle=':', label='$10^{-19}t^{15}$', color='black')
    plt.plot(t, 1e-21 * t ** 15, linestyle='-.', label='$10^{-21}t^{15}$', color='black')
    
    plt.xlabel('$t$')
    plt.ylabel('$\Delta_n$', rotation=0)
    
    plt.yscale('log')
    
    plt.xlim(0.01, 100)
    plt.ylim(10 ** -6.5, 100)
    
    plt.legend()
    
    plt.savefig('2halflog_power.eps')
    
    plt.xscale('log')
    plt.savefig('2fulllog_power.eps')


if __name__ == '__main__':
    ts2, us2 = readfile('laurents2.txt')
    ts4, us4 = readfile('laurents4.txt')
    ts6, us6 = readfile('laurents6.txt')
    
    plot_power(ts2, us2, ts4, us4, ts6, us6)
    plot_exp(ts2, us2, ts4, us4, ts6, us6)
    