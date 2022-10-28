from matplotlib import pyplot as plt

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
    ts2, us2 = readfile('laurents2.txt')
    ts4, us4 = readfile('laurents4.txt')
    ts6, us6 = readfile('laurents6.txt')
    
    fig = plt.figure(figsize=(6.4 * 2, 4.8))
    ax1 = fig.add_subplot(121)
    ax2 = fig.add_subplot(122)
    
    ax1.plot(ts2, us2, label='$n=2$', color='red')
    ax1.plot(ts4, us4, label='$n=4$', color='green')
    ax1.plot(ts6, us6, label='$n=6$', color='blue')
    
    ax2.plot(ts2, us2, label='$n=2$', color='red')
    ax2.plot(ts4, us4, label='$n=4$', color='green')
    ax2.plot(ts6, us6, label='$n=6$', color='blue')
    
    ax1.set_xlabel('$t$')
    ax2.set_xlabel('$t$')
    ax1.set_ylabel('$\Delta_n$', rotation=0)
    ax2.set_ylabel('$\Delta_n$', rotation=0)
    
    ax1.set_yscale('log')
    ax2.set_yscale('log')
    ax2.set_xscale('log')
    
    ax1.set_xlim(0, 100)
    ax2.set_xlim(0.01, 100)
    ax1.set_ylim(10 ** -6.5, 100)
    ax2.set_ylim(10 ** -6.5, 100)
    
    ax1.legend()
    ax2.legend()
    plt.tight_layout()
    
    plt.savefig('2.eps')
    