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


def plot_exp(ts2, us2, ts4, us4, ts6, us6):
    plt.cla()
    
    plt.plot(ts2, us2, label='$n=2$', color='red')
    plt.plot(ts4, us4, label='$n=4$', color='green')
    plt.plot(ts6, us6, label='$n=6$', color='blue')
    
    t = np.logspace(-2, 2)
    plt.plot(t, 1e-6 * np.exp(0.8 * t), linestyle='--', label='$10^{-6}e^{0.8t}$', color='black')
    plt.plot(t, 1e-8 * np.exp(0.8 * t), linestyle=':', label='$10^{-8}e^{0.8t}$', color='black')
    plt.plot(t, 1e-10 * np.exp(0.8 * t), linestyle='-.', label='$10^{-10}e^{0.8t}$', color='black')
    
    plt.xlabel('$t$')
    plt.ylabel('$\Delta_n$', rotation=0)
    
    plt.yscale('log')
    
    plt.xlim(0, 100)
    plt.ylim(10 ** -6.5, 100)
    
    plt.legend()
    plt.tight_layout()
    
    plt.savefig('2halflog_exp.eps')
    
    plt.xscale('log')
    plt.legend(ncol=2)
    plt.xlim(0.01, 100)
    plt.savefig('2fulllog_exp.eps')



def plot_power(ts2, us2, ts4, us4, ts6, us6):
    plt.cla()
    
    plt.plot(ts2, us2, label='$n=2$', color='red')
    plt.plot(ts4, us4, label='$n=4$', color='green')
    plt.plot(ts6, us6, label='$n=6$', color='blue')
    
    t = np.logspace(0, 2)
    plt.plot(t, 10 ** (-18.5) * t ** 15, linestyle='--', label='$10^{-18.5}t^{15}$', color='black')
    plt.plot(t, 10 ** (-20.5) * t ** 15, linestyle=':', label='$10^{-20.5}t^{15}$', color='black')
    plt.plot(t, 10 ** (-22.5) * t ** 15, linestyle='-.', label='$10^{-22.5}t^{15}$', color='black')
    
    plt.xlabel('$t$')
    plt.ylabel('$\Delta_n$', rotation=0)
    
    plt.yscale('log')
    
    plt.xlim(0, 100)
    plt.ylim(10 ** -6.5, 100)
    
    plt.legend()
    plt.tight_layout()
    
    plt.savefig('2halflog_power.eps')
    
    plt.xscale('log')
    plt.legend(ncol=2)
    plt.xlim(0.01, 100)
    plt.savefig('2fulllog_power.eps')


if __name__ == '__main__':
    ts2, us2 = readfile('laurents2.txt')
    ts4, us4 = readfile('laurents4.txt')
    ts6, us6 = readfile('laurents6.txt')
    
    plot_power(ts2, us2, ts4, us4, ts6, us6)
    plot_exp(ts2, us2, ts4, us4, ts6, us6)
    