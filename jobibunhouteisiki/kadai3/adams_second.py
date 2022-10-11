from matplotlib import pyplot as plt
from matplotlib import rc


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
    ts, us = readfile('adams_second.txt')
    
    rc('text', usetex=True)
    
    # plt.xlim(0, 1)
    # plt.ylim(0, 1.4)
    
    plt.scatter(ts, us, color='black', clip_on=False)
    plt.plot(ts, us, color='black')
    
    plt.xlabel('$\Delta t$ [s]')
    plt.ylabel('$E$', rotation=0)
    
    plt.xscale('log')
    plt.yscale('log')
    
    plt.savefig('adams_second.eps')
    