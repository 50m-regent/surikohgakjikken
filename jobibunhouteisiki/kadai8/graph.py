from matplotlib import pyplot as plt

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
    plt.plot(*readfile('R100.txt'), color='black', marker='.', label='$N=10^2$')
    plt.plot(*readfile('R1000.txt'), color='red', marker='v', label='$N=10^3$')
    
    plt.xlabel('$K$')
    plt.ylabel(r'$\bar{R}$', rotation=0)
    
    # plt.xscale('log')
    # plt.yscale('log')
    
    plt.xlim(1, 3)
    plt.ylim(0, 0.6)
    
    plt.legend()
    plt.tight_layout()
    
    plt.savefig('8.eps')
    